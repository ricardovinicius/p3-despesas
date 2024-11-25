from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, select
from src.models.user_model import User
from src.common.db import engine

class IUserRepository():
    def add(user: User) -> User:
        raise NotImplementedError
    
    def delete(user: User) -> None:
        raise NotImplementedError
    
    def get_by_email_address(email: str) -> User:
        raise NotImplementedError
    
    def get_by_id(id: int) -> User:
        raise NotImplementedError

class UserRepository(IUserRepository):
    def add(self, user: User) -> User:
        with Session(engine) as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            
            return user
            
    def get_by_email_address(self, email) -> User:
        with Session(engine) as session:
            sttm = select(User).where(User.email == email)
            user = session.exec(sttm).first()
            
            return user
    
    def get_by_id(self, id: int) -> User:
        with Session(engine) as session:
            user = session.get(User, id)
            
            return user
            
UserRepositoryDep = Annotated[IUserRepository, Depends(UserRepository)]