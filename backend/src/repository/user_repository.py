from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, select
from src.models.user_model import User
from src.common.db import engine

class IUserRepository():
    def add(user: User) -> None:
        raise NotImplementedError
    
    def delete(user: User) -> None:
        raise NotImplementedError
    
    def get_by_email_address(email_address: str) -> User:
        raise NotImplementedError

class UserRepository(IUserRepository):
    def add(self, user: User) -> None:
        with Session(engine) as session:
            session.add(user)
            session.commit()
            
    def get_by_email_address(self, email_address) -> User:
        with Session(engine) as session:
            sttm = select(User).where(User.email_address == email_address)
            user = session.exec(sttm).first()
            
            return user
            
UserRepositoryDep = Annotated[IUserRepository, Depends(UserRepository)]