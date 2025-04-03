import asyncio
import logging
from aiohttp import web
from aiohttp_swagger import setup_swagger

from app.analytics import get_summary, get_monthly, get_budget
from app.consumer import consume

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_app():
    app = web.Application()
    app.add_routes([
        web.get('/analytics/summary', get_summary),
        web.get('/analytics/monthly', get_monthly),
        web.get('/analytics/budget', get_budget),
    ])

    # Setup Swagger UI from file
    setup_swagger(app, swagger_from_file="swagger.yaml")

    return app

async def start_services():
    app = create_app()
    runner = web.AppRunner(app)
    await runner.setup()

    site = web.TCPSite(runner, '0.0.0.0', 8002)
    await site.start()
    logger.info("🌐 Analytics service running at http://0.0.0.0:8002")
    logger.info("📄 Swagger docs at http://0.0.0.0:8002/api/doc")

    await consume()  # keep this running

if __name__ == "__main__":
    try:
        asyncio.run(start_services())
    except Exception as e:
        logger.error("❌ Error starting analytics service", exc_info=True)
