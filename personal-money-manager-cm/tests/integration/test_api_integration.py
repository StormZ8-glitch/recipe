from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_create_transaction():
    response = client.post("/api/v1/transactions/", json={
        "amount": 1000,
        "category": "Food",
        "date": "2023-10-01",
        "user_id": 1
    })
    assert response.status_code == 201
    assert response.json()["amount"] == 1000

def test_get_transactions():
    response = client.get("/api/v1/transactions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_user():
    response = client.post("/api/v1/users/", json={
        "username": "testuser",
        "password": "testpassword",
        "email": "test@example.com"
    })
    assert response.status_code == 201
    assert response.json()["username"] == "testuser"

def test_get_users():
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_savings_goal():
    response = client.post("/api/v1/goals/", json={
        "goal_name": "Travel",
        "target_amount": 500000,
        "user_id": 1
    })
    assert response.status_code == 201
    assert response.json()["goal_name"] == "Travel"