from fastapi import APIRouter

from system.Config import DB_AUTH_READ
router = APIRouter()
@router.get("/")
async def root():
    return {"message": "Hello World"}
async def read_users():
    from main import dbms
    client = dbms.client(DB_AUTH_READ)
    res = client.query("SELECT * FROM test")
    print("[Data]",res)
    return {"message": f"Hello World {res}"}

@router.get("/{user_id}")
async def read_user(user_id: int):
    return {"message": f"User ID: {user_id}"}