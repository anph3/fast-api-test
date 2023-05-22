from pydantic import BaseModel, Field
from typing import Any

class ResponseData(BaseModel):
    statusCode: int = Field(default=1, alias='status')
    message: str = Field(default='Success')
    data: Any = Field(default=None)