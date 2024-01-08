from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


Base = declarative_base()

class UserModel(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  email = Column(String, unique=True)
  password = Column(String)
  role = Column(String, default="user")
  isActive = Column(Boolean)
  time_created = Column(DateTime(timezone=True), server_default=func.now())
  time_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
