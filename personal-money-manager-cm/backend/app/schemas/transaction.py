from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TransactionBase(BaseModel):
    amount: float
    category: str
    date: datetime

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(TransactionBase):
    id: int

class Transaction(TransactionBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True