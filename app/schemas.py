from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class TodoCreate(BaseModel):
    title: str = Field(..., max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    completed: Optional[bool] = False

class TodoRead(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime

    class Config:
        orm_mode = True

class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    completed: Optional[bool] = None
