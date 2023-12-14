from fastapi import APIRouter,Depends,status,Response,HTTPException
from ..hashing import Hash
from .. import schemas, models,database
from sqlalchemy.orm import Session
from ..repository import user 
from .. import oauth2
from typing import List 


router = APIRouter(
    tags=["User"],
    prefix ='/user'
    )
get_db = database.get_db


@router.get('/',response_model= List[schemas.showUser])
async def getAll(db :Session = Depends(database.get_db),get_current_user : schemas.User = Depends(oauth2.get_current_user)):
    return user.getAll(db);

@router.post ('/',response_model= schemas.showUser,status_code=status.HTTP_201_CREATED )
async def create_user (request :schemas.UserForm,db :Session = Depends(get_db),get_current_user : schemas.User = Depends(oauth2.get_current_user)):
    return user.create(request,db )

@router.get('/{id}',response_model= schemas.showUser)
async def getById(id ,response :Response ,db :Session = Depends(get_db),get_current_user : schemas.User = Depends(oauth2.get_current_user)):
    return user.getById(id,db)