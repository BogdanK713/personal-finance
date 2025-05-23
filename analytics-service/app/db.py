import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017")

def get_collection(name):
    client = AsyncIOMotorClient(MONGO_URI)
    db = client["analytics_db"]
    return db[name]
