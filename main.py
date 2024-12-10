from fastapi import FastAPI, Request
from Module.Database.DatabaseManager import DatabaseManager
from Module.Form.MessageForm import MessageForm
from Module.Logger.Logger import Logger
from Module.Session.Session import Session
from Module.Session.SessionAuth import SessionAuth
from Module.Session.SessionFunc import authSave, authMode, authHeader
from src.Router import Router
from system.Store import Store
from system.System import RunMain, RunConfig
app:FastAPI = RunMain()
store:Store = RunConfig()
dbms:DatabaseManager = store.dbms()
session:Session = store.session()
logs:Logger = store.log()
session.connect()
Router(app)
@app.get("/")
async def root():
    authSave("kds","sdf123","kms")
    form:MessageForm = MessageForm()
    cm: SessionAuth = authMode("kds","sdf123")
    if cm.status is True:
        form.status(True).message("OK").data(cm.show()).timer(True)
    return form.show()
@app.get("/test")
async def test(request:Request):
    header:dict = authHeader(request)
    print(header["sid"],header["token"])
    form:MessageForm = MessageForm()
    cm: SessionAuth = authMode(header["sid"],header["token"])
    if cm.status is True:
        form.status(True).message("OK").data(cm.show()).timer(True)
    else:
        form.status(False).message("ERROR").data(cm.show()).timer(False)
    return form.show()