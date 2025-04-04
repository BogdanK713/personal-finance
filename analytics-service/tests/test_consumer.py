import asyncio
import json
import contextlib
import pytest
import aio_pika
from motor.motor_asyncio import AsyncIOMotorClient
from app.consumer import consume

MONGO_URI = "mongodb+srv://root:root@cluster0.hixql.mongodb.net/analytics?retryWrites=true&w=majority&appName=Cluster0"  # Replace with your Atlas URI in CI
RABBITMQ_URI = "amqp://guest:guest@localhost/"
QUEUE_NAME = "transactions"

@pytest.mark.asyncio
async def test_rabbitmq_to_mongodb():
    # Start the consumer as a background task
    consumer_task = asyncio.create_task(consume())
    await asyncio.sleep(2)  # Give consumer time to connect

    # Connect to RabbitMQ and send test message
    connection = await aio_pika.connect_robust(RABBITMQ_URI)
    channel = await connection.channel()

    test_message = {
        "user_id": "testuser_integration",
        "category": "Test",
        "amount": 99.99,
        "type": "Expense",
        "date": "2025-03-30"
    }

    await channel.default_exchange.publish(
        aio_pika.Message(body=json.dumps(test_message).encode()),
        routing_key=QUEUE_NAME
    )

    # Check MongoDB for the inserted document
    client = AsyncIOMotorClient(MONGO_URI)
    db = client.analytics_db

    result = None
    for _ in range(30):  # Retry for up to 15s
        result = await db.transactions.find_one({"user_id": "testuser_integration"})
        if result:
            break
        await asyncio.sleep(0.5)

    # Cleanup
    await connection.close()
    client.close()
    consumer_task.cancel()
    with contextlib.suppress(asyncio.CancelledError):
        await consumer_task

    assert result is not None, "Message was not found in MongoDB after 15 seconds"
    assert result["amount"] == 99.99


@pytest.mark.asyncio
async def test_verify_written_document():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client.analytics_db

    # Look for the document directly
    result = await db.transactions.find_one({"user_id": "testuser_integration"})

    assert result is not None, "No document with user_id=testuser_integration found in MongoDB"
    assert result["category"] == "Test"
    assert result["amount"] == 99.99
    assert result["type"] == "Expense"

    client.close()
