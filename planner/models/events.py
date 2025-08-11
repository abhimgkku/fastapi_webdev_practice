from pydantic import BaseModel, Field

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: list[str]
    location: str
    
    class Config:
        schema_extra = {
            "example": {
                "title": "Sample Event",
                "image": "http://example.com/image.jpg",
                "description": "This is a sample event description.",
                "tags": ["tag1", "tag2"],
                "location": "Sample Location"
            }
        }