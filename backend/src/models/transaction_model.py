import datetime
from enum import Enum
from sqlmodel import Field, Relationship, SQLModel
from src.models.user_model import User

class Categoria(Enum):
    ALIMENTACAO = "ALIMENTACAO"
    TRANSPORTE = "TRANSPORTE"
    SAUDE = "SAUDE"
    EDUCACAO = "EDUCACAO"
    MORADIA = "MORADIA"
    LAZER = "LAZER"
    COMPRAS = "COMPRAS"
    CONTAS_UTILIDADES = "CONTAS_E_UTILIDADES"
    OUTROS = "OUTROS"

class Transaction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: str
    description: str
    value: float
    date: datetime.date
    category: Categoria 

    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="transactions")
