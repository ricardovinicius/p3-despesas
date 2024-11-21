import datetime
from sqlmodel import Field, Relationship, SQLModel
from src.models.user_model import User

class Transaction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: str
    description: str
    value: float
    date: datetime.date
    category: str 

    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="transactions")
