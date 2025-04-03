import os
from motor.motor_asyncio import AsyncIOMotorClient

# Get Mongo URI from environment or fallback to localhost (for local dev)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

client = AsyncIOMotorClient(MONGO_URI)
db = client.analytics_db

def get_collection(name):
    return db[name]
