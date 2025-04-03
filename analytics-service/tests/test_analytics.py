import pytest
from aiohttp import web
from app.analytics import get_summary, get_monthly, get_budget

@pytest.fixture
def app():
    app = web.Application()
    app.add_routes([
        web.get('/analytics/summary', get_summary),
        web.get('/analytics/monthly', get_monthly),
        web.get('/analytics/budget', get_budget),
    ])
    return app

async def test_get_summary(aiohttp_client, app):
    client = await aiohttp_client(app)
    resp = await client.get("/analytics/summary")
    assert resp.status == 200
    data = await resp.json()
    assert "total_transactions" in data

async def test_get_monthly(aiohttp_client, app):
    client = await aiohttp_client(app)
    resp = await client.get("/analytics/monthly")
    assert resp.status == 200
    data = await resp.json()
    assert "data" in data

async def test_get_budget(aiohttp_client, app):
    client = await aiohttp_client(app)
    resp = await client.get("/analytics/budget?user_id=testuser")
    assert resp.status == 200
    data = await resp.json()
    assert "status" in data
