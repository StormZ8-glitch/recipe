from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.models.user import User
from app.crud.user import create_user, get_user_by_username
from app.schemas.user import UserCreate

app = FastAPI()
client = TestClient(app)

def test_create_user():
    user_data = {"username": "testuser", "password": "testpassword", "email": "test@example.com"}
    response = client.post("/api/v1/users/", json=user_data)
    assert response.status_code == 201
    assert response.json()["username"] == user_data["username"]

def test_get_user():
    user_data = {"username": "testuser", "password": "testpassword", "email": "test@example.com"}
    create_user(UserCreate(**user_data))
    response = client.get("/api/v1/users/testuser")
    assert response.status_code == 200
    assert response.json()["username"] == user_data["username"]

def test_get_nonexistent_user():
    response = client.get("/api/v1/users/nonexistentuser")
    assert response.status_code == 404