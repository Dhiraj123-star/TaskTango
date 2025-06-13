from fastapi import FastAPI
from src.config import settings
from src.database import init_db
from src.routes import router as task_router
from src.auth_routes import router as auth_router
import logging

logging.basicConfig(level=settings.LOG_LEVEL)
logger = logging.getLogger(__name__)

app = FastAPI(title="TaskTango API")

app.include_router(task_router)  # Remove prefix to avoid /tasks/tasks/
app.include_router(auth_router)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting TaskTango API...")
    init_db()

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/")
async def root():
    return {"message": "Welcome to TaskTango API"}