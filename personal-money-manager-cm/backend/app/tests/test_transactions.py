from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.api.v1.endpoints.transactions import create_transaction, get_transactions, update_transaction, delete_transaction
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionUpdate

app = FastAPI()

client = TestClient(app)

def test_create_transaction():
    response = client.post("/api/v1/transactions/", json={"amount": 1000, "category": "Food", "date": "2023-10-01", "user_id": 1})
    assert response.status_code == 201
    assert response.json()["amount"] == 1000

def test_get_transactions():
    response = client.get("/api/v1/transactions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_transaction():
    response = client.put("/api/v1/transactions/1", json={"amount": 1500, "category": "Food", "date": "2023-10-01"})
    assert response.status_code == 200
    assert response.json()["amount"] == 1500

def test_delete_transaction():
    response = client.delete("/api/v1/transactions/1")
    assert response.status_code == 204
    assert response.content == b""