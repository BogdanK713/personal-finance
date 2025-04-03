import asyncio
import aio_pika
import json

async def send_test_message():
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    channel = await connection.channel()
    await channel.default_exchange.publish(
        aio_pika.Message(
            body=json.dumps({
                "user_id": "user123",
                "category": "Food",
                "amount": 25.0,
                "type": "Expense",
                "date": "2025-03-30"
            }).encode()
        ),
        routing_key="transactions"
    )

asyncio.run(send_test_message())
