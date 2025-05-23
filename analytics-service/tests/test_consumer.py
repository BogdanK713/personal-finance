import asyncio
import json
import contextlib
import os
import pytest
import aio_pika
import threading
from motor.motor_asyncio import AsyncIOMotorClient
from app.consumer import consume

MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:27017")
RABBITMQ_URI = os.getenv("AMQP_URI", "amqp://guest:guest@rabbitmq/")
QUEUE_NAME = "transactions"

def run_consumer_in_thread():
    def start():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(consume())
    thread = threading.Thread(target=start, daemon=True)
    thread.start()

async def wait_for_rabbitmq(host="rabbitmq", port=5672, timeout=15):
    for _ in range(timeout):
        try:
            reader, writer = await asyncio.open_connection(host, port)
            writer.close()
            await writer.wait_closed()
            return True
        except:
            await asyncio.sleep(1)
    raise RuntimeError("RabbitMQ not available after waiting")

@pytest.mark.asyncio
async def test_rabbitmq_to_mongodb():
    os.environ["TEST_MODE"] = "true"
    await wait_for_rabbitmq()

    run_consumer_in_thread()
    await asyncio.sleep(2)

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

    client = AsyncIOMotorClient(MONGO_URI)
    db = client.analytics_db
    result = None
    for _ in range(30):
        result = await db.transactions.find_one({"user_id": "testuser_integration"})
        if result:
            break
        await asyncio.sleep(0.5)

    await connection.close()
    client.close()
    await asyncio.sleep(1)

    assert result is not None, "Message was not found in MongoDB after 15 seconds"
    assert result["amount"] == 99.99
