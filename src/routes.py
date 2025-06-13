from fastapi import APIRouter, Depends, HTTPException
from src.models import Task, TaskCreate, TaskUpdate
from src.database import get_db
from src.auth import get_current_user
import psycopg2
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.get("/tasks/", response_model=list[Task])
async def get_tasks(conn=Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        cur = conn.cursor()
        cur.execute("SELECT id, title, description, completed, user_id FROM tasks WHERE user_id = %s", (current_user["id"],))
        tasks = cur.fetchall()
        cur.close()
        return [Task(id=row[0], title=row[1], description=row[2], completed=row[3], user_id=row[4]) for row in tasks]
    except psycopg2.Error as e:
        logger.error(f"Error fetching tasks: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/tasks/", response_model=Task)
async def create_task(task: TaskCreate, conn=Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO tasks (title, description, completed, user_id) VALUES (%s, %s, %s, %s) RETURNING id, title, description, completed, user_id",
            (task.title, task.description, task.completed, current_user["id"])
        )
        row = cur.fetchone()
        conn.commit()
        cur.close()
        return Task(id=row[0], title=row[1], description=row[2], completed=row[3], user_id=row[4])
    except psycopg2.Error as e:
        logger.error(f"Error creating task: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: TaskUpdate, conn=Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        cur = conn.cursor()
        cur.execute(
            "UPDATE tasks SET title = %s, description = %s, completed = %s WHERE id = %s AND user_id = %s RETURNING id, title, description, completed, user_id",
            (task.title, task.description, task.completed, task_id, current_user["id"])
        )
        row = cur.fetchone()
        conn.commit()
        cur.close()
        if row is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return Task(id=row[0], title=row[1], description=row[2], completed=row[3], user_id=row[4])
    except psycopg2.Error as e:
        logger.error(f"Error updating task: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int, conn=Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM tasks WHERE id = %s AND user_id = %s RETURNING id", (task_id, current_user["id"]))
        row = cur.fetchone()
        conn.commit()
        cur.close()
        if row is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return {"message": "Task deleted"}
    except psycopg2.Error as e:
        logger.error(f"Error deleting task: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")