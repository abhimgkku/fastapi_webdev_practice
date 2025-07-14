from fastapi import APIRouter
from model import Todo
todo_router = APIRouter()

todo_list = []

@todo_router.get("/todos")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}

@todo_router.post("/todos")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}

@todo_router.get("/todos/{todo_id}")
async def get_todo(todo_id: int) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "Todo not found"}
