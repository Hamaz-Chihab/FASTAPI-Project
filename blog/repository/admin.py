
from fastapi import status,HTTPException
from .. import models
from sqlalchemy.orm import Session
from ..hashing import Hash
from .. import schemas, models
from sqlalchemy.orm import Session
def getAll(db :Session):
    admins = db.query(models.Admin).all()
    return admins

def create(request  :schemas.Admin ,db :Session):
    new_admin = models.Admin(name=request.name, email=request.email, hashed_password = Hash.bcrypt(request.hashed_password),created_at=request.created_at)#refer to the db mosule Structure
    db.add(new_admin)   
    db.commit()
    db.refresh(new_admin)
    return new_admin


def getById(id,db :Session):
    result = db.query(models.Admin).filter(models.Admin.id == id).first()
    if not result : 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,Detail =f'Admin with this id = {id} is not available')
    return result


def destry(id ,db :Session ):
    db.query(models.Admin).filter(models.Admin.id == id).delete(synchronize_session=False)
    db.commit()
    return {'Admin deleted Successfuly'}

def update(id ,request :schemas.Admin ,db :Session):
    admin = db.query(models.Admin).filter(models.Admin.id == id).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,Detail =f'the Admin with id = {id} is not available')
    
    for var, value in vars(request).items():
        if value is not None:
            setattr(admin, var, value)

    db.commit()    
    return {'Admin Updated Succefully'}