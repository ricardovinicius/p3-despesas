import bcrypt
from fastapi import APIRouter, HTTPException, Security
from fastapi_jwt import JwtAuthorizationCredentials

from src.models.user_model import User
from src.repositories.user_repository import IUserRepository, UserRepository
from src.schemas.user_schemas import UserCreateSchema, UserLoginSchema
from src.repositories.user_repository import UserRepositoryDep
from src.common.security import SecurityConfig, SecurityDep

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
    
    try:
        userRepository.add(admin)
    except:
        pass

@router.post("/login")
async def login(data: UserLoginSchema, userRepository: UserRepositoryDep, security: SecurityDep):
    user: User = userRepository.get_by_email_address(data.email)
    
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    if not bcrypt.checkpw(data.password.encode('utf-8'), user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    subject = {"id": user.id, "username": user.name}
    
    access_token = security.access_security.create_access_token(subject=subject)

    return {"token": access_token}

@router.post("/")
async def create_new_user(data: UserCreateSchema, userRepository: UserRepositoryDep):
    already_registred_user: User = userRepository.get_by_email_address(data.email)
    
    if already_registred_user:
        raise HTTPException(status_code=422, detail="User with same email already registred")
    
    password = data.password
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(pwd_bytes, salt)
    
    user = User(name=data.name, email=data.email, password=hash)
    
    userRepository.add(user)

@router.get("/me")
def read_current_user(userRepository: UserRepositoryDep,
                      credentials: JwtAuthorizationCredentials = Security(SecurityConfig.access_security)):  
    if not credentials:
        raise HTTPException(status_code=401, detail='Unauthorized')
    
    user: User = userRepository.get_by_id(credentials["id"])
    
    return user