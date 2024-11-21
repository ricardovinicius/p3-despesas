from typing import Annotated
from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

from .settings import get_settings

from ..models import user_model, transaction_model

settings = get_settings()

connect_args = {"check_same_thread": False}
engine = create_engine(settings.database_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]