from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    item: str

    class Config:
        schema_extra = {          # ← all-lowercase
            "example": {          # ← all-lowercase
                "id": 1,
                "item": "Example Schema Item"
            }
        }
class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Example Todo Item"
            }
        }
class TodoItems(BaseModel):
    items: list[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "items": [
                    {"item": "Example Todo Item 1"},
                    {"item": "Example Todo Item 2"}
                ]
            }
        }
