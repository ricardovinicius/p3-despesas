from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, select
from src.models.transaction_model import Transaction
from src.common.db import engine

class ITransactionRepository():
    def add(transaction: Transaction) -> None:
        raise NotImplementedError
    
    def list(user_id) -> list[Transaction]:
        raise NotImplementedError

class TransactionRepository(ITransactionRepository):
    def add(self, transaction: Transaction) -> None:
        with Session(engine) as session:
            session.add(transaction)
            session.commit()
            
    def list(self, user_id: int) -> list[Transaction]:
        with Session(engine) as session:
            sttm = select(Transaction).where(Transaction.user_id == user_id)
            data = session.exec(sttm).all()
            
            return data
            
TransactionRepositoryDep = Annotated[ITransactionRepository, Depends(TransactionRepository)]