import pytest
from aiohttp import web
from app.main import create_app  # prilagodi pot, če je drugačna
import asyncio

# Fix za "RuntimeError: Event loop is closed" z motor/mongo
@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()

# Fixture za aiohttp aplikacijo
@pytest.fixture
def app():
    return create_app()

# --- TESTI ---

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
