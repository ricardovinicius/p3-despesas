from typing import List, Tuple, Annotated
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from src.models.goal_model import Goal
from src.schemas.goal_schema import GoalCreate, GoalRead, GoalUpdate
from src.common.db import engine

class IGoalRepository:
    def add(goal: Goal) -> None:
        raise NotImplementedError
    
    def get_by_user_id_and_category(user_id: int, category: str) -> Goal:
        raise NotImplementedError
    
    def get_goals_by_user_id(user_id: int) -> List[Goal]:
        raise NotImplementedError
    
    def get_or_create_goal_by_user_id_and_category(user_id: int, category: str) -> Goal:
        raise NotImplementedError
    
    def update_goal(goal_id: int, goal_update: GoalUpdate) -> Goal:
        raise NotImplementedError

class GoalRepository(IGoalRepository):
    def add(self, goal: Goal) -> None:
        with Session(engine) as session:
            session.add(goal)
            session.commit()
            session.refresh(goal)
    
    def get_by_user_id_and_category(self, user_id: int, category: str) -> Goal:
        with Session(engine) as session:
            goal = session.query(Goal).filter(Goal.user_id == user_id, Goal.category == category).first()
            if not goal:
                raise HTTPException(status_code=404, detail="Goal not found")
            return goal
    
    def get_goals_by_user_id(self, user_id: int) -> List[Goal]:
        with Session(engine) as session:
            return session.query(Goal).filter(Goal.user_id == user_id).all()
    
    def get_or_create_goal_by_user_id_and_category(self, user_id: int, category: str) -> Goal:
        with Session(engine) as session:
            goal = session.query(Goal).filter(Goal.user_id == user_id, Goal.category == category).first()
            if not goal:
                goal = Goal(user_id=user_id, category=category, goal=100.0)
                session.add(goal)
                session.commit()
                session.refresh(goal)
            return goal
    
    def update_goal(self, goal_id: int, goal_update: GoalUpdate) -> Goal:
        with Session(engine) as session:
            goal = session.get(Goal, goal_id)
            if not goal:
                raise HTTPException(status_code=404, detail="Goal not found")
            
            for key, value in goal_update.dict(exclude_unset=True).items():
                setattr(goal, key, value)
            
            session.commit()
            session.refresh(goal)
            return goal

GoalRepositoryDep = Annotated[IGoalRepository, Depends(GoalRepository)]
