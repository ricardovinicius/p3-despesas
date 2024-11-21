from fastapi import APIRouter, Security, HTTPException
from fastapi_jwt import JwtAuthorizationCredentials

from src.common.security import SecurityConfig
from src.models.goal_model import Goal
from src.repositories.goal_repository import GoalRepositoryDep
from src.schemas.goal_schema import GoalCreate, GoalRead, GoalUpdate

router = APIRouter(
    prefix="/goal",
    tags=["goal"]
)

@router.post("", response_model=GoalRead, status_code=201)
async def create_goal_endpoint(
    goal: GoalCreate, 
    goalRepository: GoalRepositoryDep,
    credentials: JwtAuthorizationCredentials = Security(SecurityConfig.access_security)
):
    if not credentials:
        raise HTTPException(status_code=401, detail='Unauthorized')
    
    if goal.user_id != credentials["id"]:
        raise HTTPException(status_code=401, detail='Unauthorized')
    
    goal_instance: Goal = Goal(
        user_id=goal.user_id,
        goal=goal.goal,
        category=goal.category
    )
    goalRepository.add(goal_instance)
    return goalRepository.get_by_id(goal_instance.id)

@router.get("/{category}")
async def get_or_create_goal_by_category_endpoint(
    category: str,
    user_id: int, 
    goalRepository: GoalRepositoryDep,
    credentials: JwtAuthorizationCredentials = Security(SecurityConfig.access_security)
):
    if not credentials:
        raise HTTPException(status_code=401, detail='Unauthorized')
    
    if user_id != credentials["id"]:
        raise HTTPException(status_code=401, detail='Unauthorized')
    
    return goalRepository.get_or_create_goal_by_user_id_and_category(user_id, category)

@router.put("/{category}", response_model=GoalRead)
async def update_goal_endpoint(
    category: str,
    user_id: int,  
    goal_update: GoalUpdate, 
    goalRepository: GoalRepositoryDep,
    credentials: JwtAuthorizationCredentials = Security(SecurityConfig.access_security)
):
    if not credentials:
        raise HTTPException(status_code=401, detail='Unauthorized')
    
    goal = goalRepository.get_by_user_id_and_category(user_id, category)
    if not goal or goal.user_id != credentials["id"]:
        raise HTTPException(status_code=401, detail='Unauthorized')
    
    return goalRepository.update_goal(goal.id, goal_update)
