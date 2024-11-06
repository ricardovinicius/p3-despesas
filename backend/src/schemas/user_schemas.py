from pydantic import BaseModel


class UserLoginSchema(BaseModel):
    email: str
    password: str
    
class UserCreateSchema(BaseModel):
    name: str 
    email: str
    password: str
    
class UserPublicSchema(BaseModel):
    id: int
    name: str
    email: str