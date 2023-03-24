from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Todo(BaseModel):
    title: str
    description: str = None
    completed: bool = False

todos = []

@app.get("/")
async def home():
  return {"Welcome to todo app"}

@app.post("/todos/")
async def create_todo(todo: Todo):
    todos.append(todo)
    return todo

@app.get("/todos/")
async def get_todos():
    return todos