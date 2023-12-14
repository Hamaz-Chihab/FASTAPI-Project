# SQLAlchemy models are used to interact with your database
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime,Enum
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.sql import func
from .__enum import Role
from sqlalchemy.dialects.postgresql import ARRAY




class Admin(Base):   
   __tablename__ = 'admins'
   id = Column(Integer, primary_key=True, index=True)
   name = Column(String)
   hashed_password = Column(String)
   created_at = Column(DateTime(timezone=True), server_default=func.now())
   email = Column(String, unique=True, index=True)
   is_active = Column(Boolean, default=True)
   employees = relationship("User", back_populates="boss")



class User(Base):
   __tablename__='users'
   id = Column(Integer, primary_key=True, index=True)
   name = Column(String)
   email =Column(String)
   hashed_password =Column(String)
   boss_id = Column(Integer, ForeignKey("admins.id"))
   boss = relationship("Admin", back_populates="employees")




