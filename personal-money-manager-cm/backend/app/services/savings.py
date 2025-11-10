from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.models.user import User
from app.schemas.transaction import TransactionCreate
from typing import List

class SavingsService:
    def __init__(self, db: Session):
        self.db = db

    def calculate_savings_progress(self, user: User) -> float:
        transactions = self.db.query(Transaction).filter(Transaction.user_id == user.id).all()
        total_income = sum(t.amount for t in transactions if t.category == 'income')
        total_expenses = sum(t.amount for t in transactions if t.category == 'expense')
        return total_income - total_expenses

    def get_savings_goals(self, user: User) -> List[Transaction]:
        return self.db.query(Transaction).filter(Transaction.user_id == user.id, Transaction.category == 'savings_goal').all()

    def add_savings_goal(self, user: User, goal: TransactionCreate) -> Transaction:
        new_goal = Transaction(**goal.dict(), user_id=user.id)
        self.db.add(new_goal)
        self.db.commit()
        self.db.refresh(new_goal)
        return new_goal

    def update_savings_goal(self, goal_id: int, updated_goal: TransactionCreate) -> Transaction:
        goal = self.db.query(Transaction).filter(Transaction.id == goal_id).first()
        for key, value in updated_goal.dict().items():
            setattr(goal, key, value)
        self.db.commit()
        self.db.refresh(goal)
        return goal

    def delete_savings_goal(self, goal_id: int) -> None:
        goal = self.db.query(Transaction).filter(Transaction.id == goal_id).first()
        self.db.delete(goal)
        self.db.commit()