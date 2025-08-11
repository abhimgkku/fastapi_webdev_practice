from pydantic import BaseModel, EmailStr
from typing import Optional
from models.events import Event

class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[list[Event]]
    
    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@gmail.com",
                "password": "securepassword123",
                "events":[]
            }
        }
        
class UserSignIn(BaseModel):
    email: EmailStr
    password: str
    
    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@gmail.com",
                "password": "securepassword123",
                "events":[]
            }
        }