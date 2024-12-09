from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.post("/test")
async def test(request: Request):
    # JSON 데이터를 dict 형태로 파싱
    body = await request.json()
    test_value = body.get("test")  # "test" 값 가져오기
    return {"message": f"Received: {test_value}"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
