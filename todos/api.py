from todo import todo_router
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Welcome to the Todo API"}

app.include_router(todo_router)
