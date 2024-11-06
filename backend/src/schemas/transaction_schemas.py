import datetime
from typing import Literal
from pydantic import BaseModel

TransactionType = Literal["income", "expense"]
TransactionCategory = Literal["food"]

class TransactionCreateSchema(BaseModel):
    type: TransactionType
    description: str
    value: float
    date: datetime.date
    category: TransactionCategory
    user_id: int