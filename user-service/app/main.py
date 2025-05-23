from fastapi import FastAPI
from app.routes import router
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("User Service is starting...")
app = FastAPI(title="User Service API")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

app.include_router(router)
