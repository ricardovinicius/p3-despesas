import re
import bcrypt
from fastapi import APIRouter, HTTPException, Security
from fastapi_jwt import JwtAuthorizationCredentials

from src.models.user_model import User
from src.repositories.user_repository import IUserRepository, UserRepository
from src.schemas.user_schemas import UserCreateSchema, UserLoginSchema, UserPublicSchema
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

@router.post("", status_code=201)
async def create_new_user(data: UserCreateSchema, userRepository: UserRepositoryDep) -> UserPublicSchema:
    already_registred_user: User = userRepository.get_by_email_address(data.email)
    
    regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    
    if data.name == None or len(data.name) <= 3:
        raise HTTPException(status_code=422, detail="Nome inválido")
    
    if data.email == None or not re.fullmatch(regex_email, data.email):
        raise HTTPException(status_code=422, detail="Email inválido")
    
    if data.password == None or len(data.password) <= 6:
        raise HTTPException(status_code=422, detail="Senha inválida")
    
    if already_registred_user:
        raise HTTPException(status_code=422, detail="Usuário com mesmo email já cadastrado")
    
    password = data.password
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(pwd_bytes, salt)
    
    user = User(name=data.name, email=data.email, password=hash)
    
    return userRepository.add(user)

@router.get("/me")
def read_current_user(userRepository: UserRepositoryDep,
                      credentials: JwtAuthorizationCredentials = Security(SecurityConfig.access_security)) -> UserPublicSchema:  
    if not credentials:
        raise HTTPException(status_code=401, detail='Unauthorized')
    
    user: User = userRepository.get_by_id(credentials["id"])
    
    return user