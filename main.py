from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from system.Config import dbms, database_read
from src.Logger.Logger import Log
from src.User.User import router as user_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/user")

@app.get("/")
async def root():
    client = dbms.client(database_read)
    res = client.query("SELECT * FROM test")
    Log(res)
    return {"message": f"Hello World {res}"}

@app.post("/test")
async def test(request: Request):
    body = await request.json()
    test_value = body.get("test")
    return {"message": f"Received: {test_value}"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
