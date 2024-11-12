from typing import List, Tuple, Annotated
from fastapi import Depends
from sqlmodel import Session, select, func
from src.models.transaction_model import Transaction
from src.common.db import engine

class ITransactionRepository:
    def add(transaction: Transaction) -> None:
        raise NotImplementedError
    
    def list(user_id: int) -> List[Transaction]:
        raise NotImplementedError
    
    def get_total_and_category_expenses(user_id: int) -> Tuple[float, List[Tuple[str, float]]]:
        raise NotImplementedError

class TransactionRepository(ITransactionRepository):
    def add(self, transaction: Transaction) -> None:
        with Session(engine) as session:
            session.add(transaction)
            session.commit()
            
    def list(self, user_id: int) -> List[Transaction]:
        with Session(engine) as session:
            sttm = select(Transaction).where(Transaction.user_id == user_id)
            data = session.exec(sttm).all()
            return data
    
    def get_total_and_category_expenses(self, user_id: int) -> Tuple[float, List[Tuple[str, float]]]:
        with Session(engine) as session:
            total_stmt = select(func.sum(Transaction.value)).where(Transaction.user_id == user_id)
            total = session.exec(total_stmt).one() or 0.0

            category_stmt = (
                select(Transaction.category, func.sum(Transaction.value))
                .where(Transaction.user_id == user_id)
                .group_by(Transaction.category)
            )
            category_expenses = session.exec(category_stmt).all()
            
            return total, category_expenses

TransactionRepositoryDep = Annotated[ITransactionRepository, Depends(TransactionRepository)]