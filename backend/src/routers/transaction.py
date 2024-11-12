from fastapi import APIRouter, Security, HTTPException
from fastapi_jwt import JwtAuthorizationCredentials

from src.common.security import SecurityConfig
from src.models.transaction_model import Transaction
from src.repositories.transaction_repository import TransactionRepositoryDep
from src.schemas.transaction_schemas import TransactionCreateSchema, CategoryExpenseSchema, TransactionSummarySchema


router = APIRouter(
    prefix="/transaction",
    tags=["transaction"]
)

@router.post("", status_code=201)
async def create_new_transaction(data: TransactionCreateSchema, transactionRepository: TransactionRepositoryDep,
                      credentials: JwtAuthorizationCredentials = Security(SecurityConfig.access_security)):
    if not credentials:
        raise HTTPException(status_code=401, detail='Unauthorized')
    
    if data.user_id != credentials["id"]:
        raise HTTPException(status_code=401, detail='Unauthorized')
    
    transaction: Transaction = Transaction(
        type=data.type,
        description=data.description,
        value=data.value,
        date=data.date,
        category=data.category,
        user_id=data.user_id
    )
    transactionRepository.add(transaction)
    
@router.get("")
async def list_transactions(user_id: int, transactionRepository: TransactionRepositoryDep, 
                            credentials: JwtAuthorizationCredentials = Security(SecurityConfig.access_security)):
    if not credentials:
        raise HTTPException(status_code=401, detail='Unauthorized')
    
    if user_id != credentials["id"]:
        raise HTTPException(status_code=401, detail='Unauthorized') 
    
    return transactionRepository.list(user_id)
    
@router.get("/summary", response_model=TransactionSummarySchema)
async def get_transaction_summary(user_id: int, transactionRepository: TransactionRepositoryDep, 
                                  credentials: JwtAuthorizationCredentials = Security(SecurityConfig.access_security)):
    if not credentials:
        raise HTTPException(status_code=401, detail='Unauthorized')
    
    if user_id != credentials["id"]:
        raise HTTPException(status_code=401, detail='Unauthorized') 
    
    # Retrieve total and category expenses
    total, category_expenses_data = transactionRepository.get_total_and_category_expenses(user_id)
    
    # Convert data into the Pydantic schema format
    category_expenses = [CategoryExpenseSchema(category=cat, total=amount) for cat, amount in category_expenses_data]
    
    return TransactionSummarySchema(total=total, category_expenses=category_expenses)