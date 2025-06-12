from fastapi import FastAPI
from src.config import settings
from src.database import init_db
from src.routes import router
import logging

logging.basicConfig(level=settings.LOG_LEVEL)
logger = logging.getLogger(__name__)

app = FastAPI(title="TaskTango API")

app.include_router(router)  # Remove prefix to avoid /tasks/tasks/

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