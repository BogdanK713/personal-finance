import asyncio
import json
import pytest
from motor.motor_asyncio import AsyncIOMotorClient
import aio_pika

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

    # Allow time for consumer to process
    await asyncio.sleep(2)

    # Check MongoDB
    client = AsyncIOMotorClient(MONGO_URI)
    db = client.analytics_db
    result = await db.transactions.find_one({"user_id": "testuser_integration"})

    assert result is not None
    assert result["amount"] == 99.99
