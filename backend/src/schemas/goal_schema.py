from pydantic import BaseModel
from typing import Optional

class GoalCreate(BaseModel):
    user_id: int
    goal: float = 100.0
    category: str

class GoalRead(BaseModel):
    id: int
    user_id: int
    goal: float
    category: str

    class Config:
        orm_mode: True

class GoalUpdate(BaseModel):
    goal: Optional[float] = None

    class Config:
        orm_mode: True