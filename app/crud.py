from typing import List, Optional
from sqlmodel import Session, select
from app import models

def create_todo(session: Session, *, todo_in: dict) -> models.Todo:
    todo = models.Todo(**todo_in)
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

def get_todo(session: Session, todo_id: int) -> Optional[models.Todo]:
    statement = select(models.Todo).where(models.Todo.id == todo_id)
    result = session.exec(statement).first()
    return result

def get_todos(session: Session, *, skip: int = 0, limit: int = 100) -> List[models.Todo]:
    statement = select(models.Todo).offset(skip).limit(limit)
    results = session.exec(statement).all()
    return results

def update_todo(session: Session, *, todo: models.Todo, todo_in: dict) -> models.Todo:
    for field, value in todo_in.items():
        if value is not None:
            setattr(todo, field, value)
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return todo

def delete_todo(session: Session, *, todo_id: int) -> None:
    todo = get_todo(session, todo_id)
    if not todo:
        return
    session.delete(todo)
    session.commit()
