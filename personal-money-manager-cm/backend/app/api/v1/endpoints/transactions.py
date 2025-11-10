from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.transaction import TransactionCreate, TransactionUpdate, TransactionOut
from app.crud.transaction import create_transaction, get_transactions, update_transaction, delete_transaction

router = APIRouter()

@router.post("/", response_model=TransactionOut)
def create_new_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return create_transaction(db=db, transaction=transaction)

@router.get("/", response_model=list[TransactionOut])
def read_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    transactions = get_transactions(db=db, skip=skip, limit=limit)
    return transactions

@router.put("/{transaction_id}", response_model=TransactionOut)
def update_existing_transaction(transaction_id: int, transaction: TransactionUpdate, db: Session = Depends(get_db)):
    db_transaction = update_transaction(db=db, transaction_id=transaction_id, transaction=transaction)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction

@router.delete("/{transaction_id}", response_model=dict)
def delete_existing_transaction(transaction_id: int, db: Session = Depends(get_db)):
    result = delete_transaction(db=db, transaction_id=transaction_id)
    if not result:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"detail": "Transaction deleted successfully"}