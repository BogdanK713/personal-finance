import json
import logging
import aio_pika
from app.db import get_collection

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

async def consume():
    try:
        connection = await aio_pika.connect_robust("amqp://guest:guest@rabbitmq/")
        channel = await connection.channel()
        queue = await channel.declare_queue("transactions", durable=True)

        logger.info("✅ RabbitMQ consumer started and listening...")

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    try:
                        payload = json.loads(message.body.decode())
                        logger.info(f"📥 Received message from queue: {payload}")

                        # insert to MongoDB
                        transactions = get_collection("transactions")
                        result = await transactions.insert_one(payload)

                        if result.inserted_id:
                            logger.info(f"✅ Inserted into MongoDB with ID: {result.inserted_id}")
                        else:
                            logger.warning("⚠️ Inserted document returned no ID")

                    except Exception as e:
                        logger.error(f"❌ Failed to process message: {e}")

    except Exception as e:
        logger.error(f"❌ Failed to start RabbitMQ consumer: {e}")
