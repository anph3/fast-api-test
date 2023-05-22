from pydantic import BaseModel, Field

class TodoItem(BaseModel):
    id: int
    title: str
    description: str = Field(default="")
    