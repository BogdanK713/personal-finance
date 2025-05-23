# transaction-service/app/producer.py

import pika
import json
import os
import logging

logging.basicConfig(level=logging.INFO)

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
RABBITMQ_QUEUE = "transactions"

# Setup connection and channel once (module-level singleton)
try:
    connection_params = pika.ConnectionParameters(host=RABBITMQ_HOST)
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
    logging.info("✅ RabbitMQ producer ready.")
except Exception as e:
    logging.error(f"❌ Failed to initialize RabbitMQ producer: {e}")
    connection = None
    channel = None

def publish_transaction(transaction_data):
    global connection, channel
    if not connection or connection.is_closed:
        logging.warning("🔁 Reconnecting to RabbitMQ...")
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
            channel = connection.channel()
            channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
        except Exception as e:
            logging.error(f"❌ Failed to reconnect to RabbitMQ: {e}")
            return

    try:
        message = json.dumps(transaction_data)
        channel.basic_publish(
            exchange="",
            routing_key=RABBITMQ_QUEUE,
            body=message,
            properties=pika.BasicProperties(delivery_mode=2),
        )
        logging.info(f"📤 Published transaction to queue: {message}")
    except Exception as e:
        logging.error(f"❌ Failed to publish transaction: {e}")
