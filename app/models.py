from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel

class TodoBase(SQLModel):
    title: str = Field(index=True, max_length=200)
    description: Optional[str] = Field(default=None, max_length=1000)
    completed: bool = Field(default=False)

class Todo(TodoBase, table=True):
    __tablename__ = "todos"
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
