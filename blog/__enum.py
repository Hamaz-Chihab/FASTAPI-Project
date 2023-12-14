
from sqlalchemy import Enum
# from enum import Enum



class Role(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"
    AVOCAT ="Avocat"
