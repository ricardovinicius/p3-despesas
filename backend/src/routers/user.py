from typing import Annotated
import bcrypt
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import select

from src.common.settings import Settings, get_settings
from src.models.user_model import User
from src.schemas.user_schemas import UserLoginSchema
from src.common.db import SessionDep

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

async def create_admin_user(session: SessionDep):
    password = 'admin'
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(pwd_bytes, salt)
    
    admin = User(name="admin", email_address="admin@admin.com", password=hash)
    
    session.add(admin)
    

@router.get("/login")
async def login(data: UserLoginSchema, session: SessionDep):
    sttm = select(User).where(User.email_address == data.email_address)
    user = session.exec(sttm)
    
    if (user is None):
        return HTTPException()
    
    return data