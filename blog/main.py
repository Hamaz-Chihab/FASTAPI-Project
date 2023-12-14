from fastapi import FastAPI
from . import models
from .database import engine
from sqlalchemy.ext.declarative import declarative_base
from .routers import user ,admin,Authentication
app = FastAPI()
models.Base.metadata.create_all(engine)



app.include_router(admin.router)
app.include_router(user.router)
app.include_router(Authentication.router)
#  The fields in this model also match the fields in the Pydantic model, but they are used in a different part of your application
Base = declarative_base()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db 
#     finally:
#         db.close()
#Create Admin ()     
# @app.post('/admin',status_code=status.HTTP_201_CREATED,tags=["Admin"])
# async def create_admin(request :schemas.Admin,db :Session = Depends(get_db)):
#     new_admin = models.Admin(name=request.name, email=request.email, hashed_password = Hash.bcrypt(request.hached_password),created_at=request.created_at)#refer to the db mosule Structure
#     db.add(new_admin)   
#     db.commit()
#     db.refresh(new_admin)
#     return new_admin
#display All()
# @app.get('/admin',response_model= List[schemas.showAdmin],tags=["Admin"])
# async def getAll(db :Session = Depends(get_db)):
#     admins = db.query(models.Admin).all()
#     return admins

#display specifique()
# @app.get('/admin/{id},',response_model= schemas.showAdmin,tags=["Admin"])
# # async def getById(id :int , nom : str | None = Query(default=None, max_length=50) ,prenom :Annotated[list[str], Query()] = ["foo", "bar"] ,db :Session = Depends(get_db)):
# async def getById(id :int ,db :Session = Depends(get_db)):
#     result = db.query(models.Admin).filter(models.Admin.id == id).first()
#     if not result : 
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,Detail =f'Admin with this id = {id} is not available')
#     return result


# @app.delete('/admin/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=["Admin"])
# async def destroy(id ,db :Session = Depends(get_db)) :
#     db.query(models.Admin).filter(models.Admin.id == id).delete(synchronize_session=False)
#     db.commit()
#     return {'Admin deleted Successfuly'}

#update Admin ()
# @app.put('/admin/{id}',status_code=status.HTTP_202_ACCEPTED,tags=["Admin"])
# async def update(id :int ,request :schemas.Admin ,db :Session = Depends(get_db)):
#     admin = db.query(models.Admin).filter(models.Admin.id == id).first()
#     if not admin:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,Detail =f'the Admin with id = {id} is not available')
    
#     for var, value in vars(request).items():
#         if value is not None:
#             setattr(admin, var, value)

#     db.commit()    
#     return {'Admin Updated Succefully'}
    


# @app.post ('/user',response_model= schemas.showUser,status_code=status.HTTP_201_CREATED,tags=["User"])
# async def create_user (request :schemas.User,db :Session = Depends(get_db)):
#     new_user = models.User(name =request.name,email =request.email,password = Hash.bcrypt(request.password),boss_id=1);#refer to the db mosule Structure
#     db.add(new_user)   
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user/{id}',response_model= schemas.showUser,tags=["User"])
# async def getById(id ,response :Response ,db :Session = Depends(get_db)):
#     result = db.query(models.User).filter(models.User.id == id).first()
#     if not result : 
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,Detail =f'Admin with this id = {id} is not available')
#     return result