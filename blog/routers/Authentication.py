from fastapi import APIRouter,Depends,status,HTTPException
from ..hashing import Hash
from .. import  models,database,JWTtoken,schemas
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm


router =APIRouter()
get_db = database.get_db
#important remarque in this case i define the respense as a showUser pydentic model in the first line so it raise an error 
# @router.post('/Login',response_model= schemas.showUser)
# def login(request :schemas.Login,db :Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.email == request.name ).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,Detail ="invalid creadentials")
#     if not Hash.verify(request.password,user.hashed_password):
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail ="incorrect password")
#     access_token = JWTtoken.create_access_token(data={"sub": user.email})
#     return {"access_token": access_token, "token_type": "bearer"}


@router.post('/Login')
def login(request:OAuth2PasswordRequestForm =Depends() ,db :Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username ).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,Detail ="invalid creadentials")
    if not Hash.verify(request.password,user.hashed_password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail ="incorrect password")
    access_token = JWTtoken.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
    #generate the JWT token and return 

