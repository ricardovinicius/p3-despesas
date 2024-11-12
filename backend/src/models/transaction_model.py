import datetime
from enum import Enum
from sqlmodel import Field, Relationship, SQLModel
from src.models.user_model import User

class Categoria(Enum):
    ALIMENTACAO = "Alimentação"
    TRANSPORTE = "Transporte"
    SAUDE = "Saúde"
    EDUCACAO = "Educação"
    MORADIA = "Moradia"
    LAZER = "Lazer"
    COMPRAS = "Compras"
    ASSINATURAS_SERVICOS = "Assinaturas e Serviços"
    CONTAS_UTILIDADES = "Contas e Utilidades"
    OUTROS = "Outros"

class Transaction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: str
    description: str
    value: float
    date: datetime.date
    category: Categoria 

    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="transactions")
