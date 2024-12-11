from fastapi import FastAPI
from src.User import router as user_router
from src.Auth import router as auth_router
def Router(app:FastAPI):
    app.include_router(user_router, prefix="/user", tags=["user"])
    app.include_router(auth_router, prefix="/auth", tags=["auth"])