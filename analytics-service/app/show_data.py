import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def show_transactions():
    client = AsyncIOMotorClient("mongodb+srv://root:root@cluster0.hixql.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client["analytics_db"]
    docs = await db.transactions.find().to_list(length=100)

    print("💾 Stored Transactions:")
    for doc in docs:
        print(doc)

if __name__ == "__main__":
    asyncio.run(show_transactions())
