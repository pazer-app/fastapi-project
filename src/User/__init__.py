from fastapi import APIRouter
from Module.Form.MessageForm import MessageForm
from system.Config import MESSAGE_RESPONSE
router = APIRouter()

# API START
@router.get("/", responses=MESSAGE_RESPONSE)
async def root():
    form:MessageForm = MessageForm()
    form.status(True).message("hi").statusCode(200).timer(True)
    return form.json()
# API END


# async def read_users():
#     from main import dbms
#     client = dbms.client(DB_AUTH_READ)
#     res = client.query("SELECT * FROM PZ_SEC_CODE")
#     print("[Data]",res)
#     return {"message": f"Hello World {res}"}
#
# @router.get("/{user_id}")
# async def read_user(user_id: int):
#     return {"message": f"User ID: {user_id}"}