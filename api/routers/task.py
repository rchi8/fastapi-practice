from typing import List

from fastapi import APIRouter 

import api.schemas.task as task_schema



router = APIRouter()


@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks():
    return [task_schema.Task(id=1, title="はじめてのtodoタスク")]



@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_task(task_id: int, task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=task_id, **task_body.dict())


@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int):
    return

@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def creat_task(task_body: task_schema.TaskCreate):
    return task_schema.TaskCreateResponse(id=1, **dict(task_body))