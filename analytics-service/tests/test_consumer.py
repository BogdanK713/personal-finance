import asyncio
import json
import pytest
from motor.motor_asyncio import AsyncIOMotorClient
import aio_pika
import time

MONGO_URI = "mongodb://localhost:27017"
RABBITMQ_URI = "amqp://guest:guest@localhost/"
QUEUE_NAME = "transactions"

@pytest.mark.asyncio
async def test_rabbitmq_to_mongodb():
    # Connect to RabbitMQ
    connection = await aio_pika.connect_robust(RABBITMQ_URI)
    channel = await connection.channel()

    # Create test message
    test_message = {
        "user_id": "testuser_integration",
        "category": "Test",
        "amount": 99.99,
        "type": "Expense",
        "date": "2025-03-30"
    }

    # Send message
    await channel.default_exchange.publish(
        aio_pika.Message(body=json.dumps(test_message).encode()),
        routing_key=QUEUE_NAME
    )

    # Poll MongoDB with retries for up to 10 seconds
    client = AsyncIOMotorClient(MONGO_URI)
    db = client.analytics_db

    for _ in range(20):  # retry every 0.5s for up to 10s
        result = await db.transactions.find_one({"user_id": "testuser_integration"})
        if result:
            break
        await asyncio.sleep(0.5)

    assert result is not None, "Message was not found in MongoDB after 10 seconds"
    assert result["amount"] == 99.99
