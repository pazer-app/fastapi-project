from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from Module.Database.DatabaseManager import DatabaseManager
from Module.Form.MessageForm import MessageForm
from Module.Logger.Logger import Logger
from Module.Session.Session import Session
from src.Router import Router
from src.User.UserForm import UserForm
from src.User.UserFunc import UserNo, UserNameChange, UserSexChange, UserStatusChange
from system.Config import MESSAGE_RESPONSE
from system.Store import Store
from system.System import RunMain, RunConfig

# MAIN - START
app:FastAPI = RunMain()
store:Store = RunConfig()
dbms:DatabaseManager = store.dbms()
session:Session = store.session()
logs:Logger = store.log()
session.connect()
Router(app)
# MAIN - END

# SCRIPT - START
vm:UserForm = UserNo(10000001)
print(vm.show())
vp= UserStatusChange(10000001,0)
if vp is not None:
    if vp is True:
        print("OK")
    else:
        print("None Change")

# SCRIPT - END

# API - START
@app.get("/",  responses=MESSAGE_RESPONSE)
async def root():
    form:MessageForm = MessageForm()
    form.status(True).message("PazerAPI Version 1.0").statusCode(200)
    return form.json()
@app.exception_handler(404)
async def custom_404_handler(request:Request, exc):
    form:MessageForm = MessageForm()
    form.status(False).message("The requested API command does not exist.").statusCode(404)
    return form.json()
@app.exception_handler(RequestValidationError)
async def custom_422_handler(request: Request, exc: RequestValidationError):
    form = MessageForm()
    msgData = {}
    for error in exc.errors():
        loc_parts = list(error["loc"])
        msg = error["msg"]
        current = msgData
        for part in loc_parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        final_key = loc_parts[-1]
        if final_key not in current:
            current[final_key] = msg
        else:
            current[final_key] += f"; {msg}"
    form.status(False)\
        .message("Execution cannot proceed due to invalid input.").statusCode(422).error(msgData)
    return form.json()
# API - END

# async def root():
#     authSave("kds","sdf123","kms")
#     form:MessageForm = MessageForm()
#     cm: SessionAuth = authMode("kds","sdf123")
#     if cm.status is True:
#         form.status(True).message("OK").data(cm.show()).timer(True)
#     return form.show()
# @app.get("/test")
# async def test(request:Request):
#     header:dict = authHeader(request)
#     print(header["sid"],header["token"])
#     form:MessageForm = MessageForm()
#     cm: SessionAuth = authMode(header["sid"],header["token"])
#     if cm.status is True:
#         form.status(True).message("OK").data(cm.show()).timer(True)
#     else:
#         form.status(False).message("ERROR").data(cm.show()).timer(False)
#     return form.show()