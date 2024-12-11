from fastapi import APIRouter
from Module.Form.MessageForm import MessageForm
from system.Config import MESSAGE_RESPONSE
router = APIRouter()

# API START
@router.get("/", responses=MESSAGE_RESPONSE)
async def root():
    form:MessageForm = MessageForm()
    form.status(True).message("OK").statusCode(200).timer(True)
    return form.json()
# API END


# async def read_users():
#     from main import dbms
#     client = dbms.client(DB_AUTH_READ)
#     res = client.query("SELECT * FROM PZ_USER")
#     print("[Data]",res)
#     return {"message": f"Hello World {res.show()}"}
#
# @router.get("/logout")
# async def logout(
#         auth: AuthHeaders = Depends()
# ):
#     form:MessageForm = MessageForm()
#     form.status(True).message(f"{auth.token} / {auth.sid}").timer(True)
#     return form.json()
#
# @router.get("/login", responses=MESSAGE_RESPONSE)
# async def login(types:int, name:str):
#     res = searchUser(types, name)
#     res.statusCode(200)
#     return res.json()
