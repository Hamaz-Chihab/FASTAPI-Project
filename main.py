# from fastapi import FastAPI
# from typing import Optional
# from pydantic import BaseModel, EmailStr

# app = FastAPI()

# class admin(BaseModel):
#     _id :int
#     full_name : str
#     email :Optional[str]

# @app.post("/admin")
# def create_profil(request :admin ):
#    return {'data' :f'hello ther, your are {request.full_name}'}



# @app.get("/admin")
# def index(limit :int =5 ,adProfile :bool =True,sort:Optional[str] =None):
#    if adProfile:
#         return {"data":f'{limit} profils have to display'}
#    else:
#        return{f'yo need to check admin profile value is :{adProfile}'}



# @app.get("/admin/{admin_id}")
# def abc(admin_id :int ):
#    return {'data' :admin_id }


# @app.get("/admin/{admin_id}/comments")
# def comment(admin_id):
#    return {'data' :{'1','2'} }
