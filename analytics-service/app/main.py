import logging
from aiohttp import web
from app.analytics import get_summary, get_monthly, get_budget
from app.consumer import consume

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def health_check(request):
    return web.json_response({"status": "ok"})

# Create aiohttp app and routes
def create_app():
    app = web.Application()
    app.router.add_get("/health", health_check)
    
    # Register analytics routes
    app.router.add_get('/analytics/summary', get_summary)
    app.router.add_get('/analytics/monthly', get_monthly)
    app.router.add_get('/analytics/budget', get_budget)

    # Register background consumer
    app.on_startup.append(start_background_tasks)
    app.on_cleanup.append(cleanup_background_tasks)

    return app

# Define background task for RabbitMQ consumer
async def start_background_tasks(app):
    logger.info("🔄 Starting RabbitMQ consumer task...")
    app['consumer_task'] = app.loop.create_task(consume())

async def cleanup_background_tasks(app):
    logger.info("🧹 Cleaning up RabbitMQ consumer task...")
    consumer_task = app.get('consumer_task')
    if consumer_task:
        consumer_task.cancel()
        try:
            await consumer_task
        except asyncio.CancelledError:
            logger.info("✅ Consumer task cancelled cleanly")

if __name__ == "__main__":
    logger.info("🌐 Starting Analytics Service...")
    web.run_app(create_app(), host="0.0.0.0", port=8002)
