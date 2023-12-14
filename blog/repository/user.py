from fastapi import status,HTTPException
from .. import models
from sqlalchemy.orm import Session
from ..hashing import Hash
from .. import schemas, models
from sqlalchemy.orm import Session

def getAll(db :Session):
    users = db.query(models.User).all()
    return users


def create(request :schemas.UserForm,db :Session ):
    new_user = models.User(name =request.name,email =request.email,hashed_password = Hash.bcrypt(request.hashed_password),boss_id=request.boss_id);#refer to the db mosule Structure
    db.add(new_user)   
    db.commit()
    db.refresh(new_user)
    return new_user

def getById(id ,db :Session) :
    result = db.query(models.User).filter(models.User.id == id).first()
    if not result : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,Detail =f'Admin with this id = {id} is not available')
    return result