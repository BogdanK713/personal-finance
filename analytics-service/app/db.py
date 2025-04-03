import os
from motor.motor_asyncio import AsyncIOMotorClient

# Use environment variable or fallback to localhost for dev
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# This works for both local Mongo and GitHub Actions service container
client = AsyncIOMotorClient(MONGO_URI)
db = client["analytics_db"]

def get_collection(name):
    return db[name]
