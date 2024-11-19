import datetime
from typing import Literal,  List
from pydantic import BaseModel

TransactionType = Literal["income", "expense"]
TransactionCategory = Literal[
    "ALIMENTACAO", 
    "TRANSPORTE", 
    "SAUDE", 
    "EDUCACAO", 
    "MORADIA", 
    "LAZER", 
    "COMPRAS", 
    "CONTAS_E_UTILIDADES", 
    "OUTROS"
]


class TransactionCreateSchema(BaseModel):
    type: TransactionType
    description: str
    value: float
    date: datetime.date
    category: TransactionCategory
    user_id: int
    
    
class CategoryExpenseSchema(BaseModel):
    category: str
    total: float


class TransactionSummarySchema(BaseModel):
    total: float
    category_expenses: List[CategoryExpenseSchema]
