import asyncio
import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017")

async def show_transactions():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client["analytics_db"]
    docs = await db.transactions.find().to_list(length=100)

    print("💾 Stored Transactions:")
    for doc in docs:
        print(doc)

if __name__ == "__main__":
    asyncio.run(show_transactions())
