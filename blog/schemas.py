# Pydantic models are used for data validation and serialization. When you receive a request in your FastAPI application
from pydantic import BaseModel
from datetime import datetime,date
from pydantic import BaseModel
from typing import Optional

class showUser(BaseModel):
    name:Optional[str]
    email:Optional[str]
    boss_id:int 
    class Config():
        orm_mode =True
class ShowUserWithAdmin(BaseModel):
    name:Optional[str]
    email:Optional[str]
    class Config():
        orm_mode =True

class showAdmin(BaseModel):
    name: str
    email:Optional[str]
    employees: list[ShowUserWithAdmin] = []

    class Config():
         orm_mode =True

class Admin(BaseModel):
    name: str
    email: str
    hashed_password :str
    created_at: datetime


class User(BaseModel):
   name: str
   email: str
   hashed_password: str
   boss_id :int

class UserForm(User):
   JobTitle: str
   Department: str
   Manager: str
   PhoneNumber: str
   DateofBirth: date
   StartDate: date
   EndDate: Optional[date]
   Address: str
   phoneNumber: str
   

class Login(BaseModel):
    email :str 
    password :str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] | None = None 




