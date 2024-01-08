from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db

from src.utils.auth import get_current_user

from ..schema.user import UserSchema, UserUpdateSchema
from ..models.user import UserModel

from ..utils.password import Hasher

router = APIRouter(
  prefix="/users",
  tags=["users"]
)


@router.post('/create', response_model=UserSchema)
def create(user: UserSchema):
  hashed_pass = Hasher.get_password_hash(user.password)

  user = UserModel(name=user.name, email=user.email, password=hashed_pass, role=user.role, isActive=user.isActive)

  db.session.add(user)
  db.session.commit()
  
  return user

@router.get('/all')
def get_users():
  users = db.session.query(UserModel).all()
  return users

@router.put('/{id}', response_model=UserSchema)
def update_user(id: int, item: UserUpdateSchema, current_user = Depends(get_current_user)):
    if current_user.role != 'admin':
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    user = db.session.query(UserModel).filter(UserModel.id == id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = item.model_dump(exclude_unset=True)
    
    if 'password' in update_data:
        update_data['password'] = Hasher.get_password_hash(update_data['password'])

    for field, value in update_data.items():
        setattr(user, field, value)

    db.session.commit()

    return user

@router.delete('/{id}', response_model=UserSchema)
def delete_user(id: int, item: UserSchema, current_user = Depends(get_current_user)):
    if current_user.role != 'admin':
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    user = db.session.query(UserModel).filter(UserModel.id == id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.session.delete(user)
    db.session.commit()

    return user


