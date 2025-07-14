from fastapi import APIRouter, Path, HTTPException, status, Request,Depends
from fastapi.templating import Jinja2Templates
from model import Todo, TodoItem, TodoItems
todo_router = APIRouter()

todo_list = []

templates = Jinja2Templates(directory="templates/")

@todo_router.get("/todos", response_model=TodoItems)
async def retrieve_todos() -> dict:
    return {"items": todo_list}

@todo_router.post("/todos", status_code=201)
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}

@todo_router.get("/todos/{todo_id}")
async def get_todo(todo_id: int = Path(...,title="The Id of the Todo to retrieve")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo with supplied id not found")

@todo_router.put("/todos/{todo_id}")
async def update_todo(todo_item: TodoItem, todo_id: int = Path(... , title="The Id of the Todo to be updated")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_item.item
            return {"message": "Todo updated successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo with supplied id not found")

@todo_router.delete("/todos/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
  for index in range(len(todo_list)):
      if todo_list[index].id == todo_id:
          del todo_list[index]
          return {"message": "Todo deleted successfully"}
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo with supplied id not found")

@todo_router.delete("/todos")
async def delete_all_todos() -> dict:
    todo_list.clear()
    return {"message": "All todos deleted successfully"}
