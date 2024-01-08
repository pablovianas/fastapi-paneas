    
from fastapi_sqlalchemy import db
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status


import os
from dotenv import load_dotenv
from src.models.user import UserModel
from src.schema.auth import TokenData

load_dotenv(".env")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

from datetime import datetime, timedelta

from jose import jwt
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=int(os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"]))
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, os.environ["SECRET_KEY"], algorithm=os.environ["ALGORITHM"])
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    
    try:
        payload = jwt.decode(token, os.environ["SECRET_KEY"], algorithms=os.environ["ALGORITHM"])
        username: str = payload.get('sub')
        if not username:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = db.session.query(UserModel).where(UserModel.email == token_data.username).first()

    if user is None:
        raise credentials_exception

    return user