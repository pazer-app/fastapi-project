from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from Module.Database.DatabaseHost import DatabaseHost
from system.Config import LoggerEnable, DatabaseHostInfo, SessionHostInfo, SystemConfig, DB_SPACE
from system.Store import Store
def RunMain()->FastAPI:
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=SystemConfig.get("allow_origins"),
        allow_credentials=SystemConfig.get("allow_credentials"),
        allow_methods=SystemConfig.get("allow_methods"),
        allow_headers=SystemConfig.get("allow_headers"),
    )
    return app
def RunConfig()->Store:
    store:Store = Store()
    store.log().enable(LoggerEnable)
    for name, data in DatabaseHostInfo.items():
        form:DatabaseHost = DatabaseHost()
        form.hostname = data.get("hostname")
        form.username = data.get("username")
        form.password = data.get("password")
        form.database = data.get("database")
        form.port = data.get("port")
        form.charset = data.get("charset")
        store.dbms().hostForm(name, form)
    store.session().host().hostname = SessionHostInfo.get("hostname")
    store.session().host().port = SessionHostInfo.get("port")
    store.session().host().namespace = SessionHostInfo.get("namespace")
    store.session().host().decode = SessionHostInfo.get("decode")
    return store
def DBSpace(table:str)->str:
    return f"{DB_SPACE}_{table}"