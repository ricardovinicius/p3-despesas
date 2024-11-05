import bcrypt
from fastapi import APIRouter, HTTPException

from src.models.user_model import User
from src.repositories.user_repository import IUserRepository, UserRepository
from src.schemas.user_schemas import UserCreateSchema, UserLoginSchema
from src.repositories.user_repository import UserRepositoryDep
from src.common.security import SecurityDep

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

def create_admin_user(userRepository: IUserRepository = UserRepository()):
    password = 'admin'
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(pwd_bytes, salt)
    
    admin = User(name="admin", email="admin@admin.com", password=hash)
    
    userRepository.add(admin)

@router.post("/login")
async def login(data: UserLoginSchema, userRepository: UserRepositoryDep, security: SecurityDep):
    user: User = userRepository.get_by_email_address(data.email)
    
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    if not bcrypt.checkpw(data.password.encode('utf-8'), user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    subject = {"username": user.name}
    
    access_token = security.access_security.create_access_token(subject=subject)

    return {"token": access_token}

@router.post("/")
async def create_new_user(data: UserCreateSchema, userRepository: UserRepositoryDep):
    password = data.password
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(pwd_bytes, salt)
    
    user = User(name=data.name, email=data.email, password=hash)
    
    userRepository.add(user)
    
    return user