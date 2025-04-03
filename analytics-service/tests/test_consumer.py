import asyncio
import json
import pytest
import aio_pika
from motor.motor_asyncio import AsyncIOMotorClient
from app.consumer import consume

MONGO_URI = "mongodb://localhost:27017"
RABBITMQ_URI = "amqp://guest:guest@localhost/"
QUEUE_NAME = "transactions"

@pytest.mark.asyncio
async def test_rabbitmq_to_mongodb():
    # Start the consumer as a background task
    consumer_task = asyncio.create_task(consume())
    await asyncio.sleep(2)  # Let the consumer connect and start listening

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
