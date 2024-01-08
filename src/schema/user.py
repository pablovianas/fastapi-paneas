from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class UserSchema(BaseModel):
    name: str
    email: str
    password: str
    role: Optional[str] = None
    isActive: bool

    class Config:
      orm_mode = True


class UserUpdateSchema(BaseModel):
  name: Optional[str] = None
  email: Optional[str] = None
  password: Optional[str] = None
  role: Optional[str] = None
  isActive: Optional[bool] = None

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(alias="username")
    password: str 