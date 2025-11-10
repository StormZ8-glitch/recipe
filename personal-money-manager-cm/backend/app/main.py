from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import transactions, users, goals
from app.core.config import settings

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update this to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(transactions.router, prefix="/api/v1/transactions", tags=["transactions"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(goals.router, prefix="/api/v1/goals", tags=["goals"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Personal Money Management App API!"}