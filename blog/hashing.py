from passlib.context import CryptContext
pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated ="auto");

class Hash():
    def bcrypt(hashed_password: str):
        return  pwd_cxt.hash(hashed_password)
    def verify(plain_password,hashed_password ,):
        return  pwd_cxt.verify(plain_password,hashed_password)#the order is important

