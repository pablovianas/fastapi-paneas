from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db

from fastapi.security import OAuth2PasswordRequestForm
from src.schema.auth import Token
from src.utils.auth import create_access_token
from src.utils.password import Hasher
from src.models.user import UserModel


router = APIRouter(
  tags=["auth"]
)


@router.post('/token', response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
):
    user = db.session.query(UserModel).where(UserModel.email == form_data.username).first()

    if not user:
        raise HTTPException(
            status_code=400, detail='Incorrect email or password'
        )

    if not Hasher.verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=400, detail='Incorrect email or password'
        )

    access_token = create_access_token(data={'sub': user.email})

    return {'access_token': access_token, 'token_type': 'bearer'}