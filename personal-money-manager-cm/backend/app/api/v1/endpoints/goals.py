from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.goal import GoalCreate, GoalRead
from app.models.goal import Goal
from app.crud.goal import create_goal, get_goals, get_goal

router = APIRouter()

@router.post("/", response_model=GoalRead)
def create_new_goal(goal: GoalCreate, db: Session = Depends(get_db)):
    return create_goal(db=db, goal=goal)

@router.get("/", response_model=list[GoalRead])
def read_goals(db: Session = Depends(get_db)):
    return get_goals(db=db)

@router.get("/{goal_id}", response_model=GoalRead)
def read_goal(goal_id: int, db: Session = Depends(get_db)):
    db_goal = get_goal(db=db, goal_id=goal_id)
    if db_goal is None:
        raise HTTPException(status_code=404, detail="Goal not found")
    return db_goal