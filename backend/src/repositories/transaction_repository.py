from typing import Annotated
from fastapi import Depends
from sqlmodel import Session
from src.models.transaction_model import Transaction
from src.common.db import engine

class ITransactionRepository():
    def add(transaction: Transaction) -> None:
        raise NotImplementedError

class TransactionRepository(ITransactionRepository):
    def add(self, transaction: Transaction) -> None:
        with Session(engine) as session:
            session.add(transaction)
            session.commit()
            
TransactionRepositoryDep = Annotated[ITransactionRepository, Depends(TransactionRepository)]