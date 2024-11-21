from sqlmodel import Field, Relationship, SQLModel
from src.models.user_model import User

class Goal(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    goal: float
    category: str

    user: User = Relationship(back_populates="goals")