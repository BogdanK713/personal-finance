import asyncio
import logging
from aiohttp import web
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
    return app

async def start_services():
    app = create_app()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', 8002)
    await site.start()

    logger.info("🌐 Analytics service running at http://0.0.0.0:8002")

    # ✅ Start consumer as a background task
    asyncio.create_task(consume())

    # 🔁 Keep app running
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    try:
        asyncio.run(start_services())
    except Exception:
        logger.error("❌ Error starting analytics service", exc_info=True)
