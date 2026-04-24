import uvicorn
from fastapi import FastAPI
from app.routers import todo
from app import database

app = FastAPI(title="Todo API", version="1.0.0")

# Register routers
app.include_router(todo.router, prefix="/todos", tags=["todos"])

# Ensure database is initialized on startup
@app.on_event("startup")
def startup():
    database.init_db()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
