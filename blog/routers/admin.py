from fastapi import APIRouter,Depends,status,HTTPException
from ..hashing import Hash
from .. import schemas, models,database
from typing import List 
from sqlalchemy.orm import Session
from ..repository import admin
from .. import oauth2
router =APIRouter(
    prefix ='/admin',
    tags=["Admin"])
get_db = database.get_db

@router.get('/',response_model= List[schemas.showAdmin] )
async def getAll(db :Session = Depends(get_db)):
    return admin.getAll(db);

@router.post('/',status_code=status.HTTP_201_CREATED )
async def create_admin(request  :schemas.Admin,db :Session = Depends(get_db)):
    return admin.create(request,db)

@router.get('/{id},',response_model= schemas.showAdmin)
# async def getById(id :int , nom : str | None = Query(default=None, max_length=50) ,prenom :Annotated[list[str], Query()] = ["foo", "bar"] ,db :Session = Depends(get_db)):
async def getById(id :int ,db :Session = Depends(get_db)):
    return admin.getById(id,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT )
async def destroy(id ,db :Session = Depends(get_db)) :
    return admin.destry(id ,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED )
async def update(id :int ,request :schemas.Admin ,db :Session = Depends(get_db)):
    return admin.update(id ,request,db )