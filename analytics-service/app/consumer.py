import asyncio
import json
import logging
import aio_pika
from .db import get_collection
import os

logger = logging.getLogger(__name__)

async def consume():
    logger.info("📡 Connecting to RabbitMQ...")
    connection = await aio_pika.connect_robust(os.getenv("AMQP_URI", "amqp://guest:guest@localhost/"))

    channel = await connection.channel()
    queue = await channel.declare_queue("transactions", durable=True)

    logger.info("✅ RabbitMQ Consumer started")

    async with queue.iterator() as q:
        async for message in q:
            async with message.process():
                try:
                    data = json.loads(message.body.decode())
                    logger.info("📥 Received message: %s", data)
                    await get_collection("transactions").insert_one(data)
                except Exception as e:
                    logger.error("❌ Error processing message", exc_info=True)
