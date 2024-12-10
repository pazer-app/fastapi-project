from fastapi import APIRouter
from system.Config import database_read, dbms
router = APIRouter()
@router.get("/")
async def read_users():
    client = dbms.client(database_read)
    res = client.query("SELECT * FROM test")
    print("[Data]",res)
    return {"message": f"Hello World {res}"}

@router.get("/{user_id}")
async def read_user(user_id: int):
    return {"message": f"User ID: {user_id}"}