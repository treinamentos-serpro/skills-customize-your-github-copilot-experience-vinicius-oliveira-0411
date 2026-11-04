from fastapi import FastAPI, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")


class TaskInput(BaseModel):
    title: str = Field(min_length=1)
    completed: bool = False


class Task(TaskInput):
    id: int


# The in-memory store resets whenever the server restarts.
tasks: list[Task] = []
next_task_id = 1


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    # TODO: Return all tasks.
    pass


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_input: TaskInput):
    # TODO: Create a task, assign an ID, and return it.
    pass


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    # TODO: Find and return the task, or respond with 404.
    pass


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_input: TaskInput):
    # TODO: Update the task, or respond with 404.
    pass


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    # TODO: Delete the task, respond with 404 if missing, and return an empty response.
    pass
