from aiohttp import web
from .db import get_collection

async def get_summary(request):
    transactions = get_collection("transactions")
    total = await transactions.count_documents({})
    return web.json_response({"total_transactions": total})

async def get_monthly(request):
    transactions = get_collection("transactions")
    cursor = transactions.find({})
    data = await cursor.to_list(length=100)
    return web.json_response({"data": data})

async def get_budget(request):
    transactions = get_collection("transactions")
    user_id = request.query.get("user_id")
    monthly_budget = 500  # Hardcoded for example

    pipeline = [
        {"$match": {"user_id": user_id, "type": "Expense"}},
        {"$group": {"_id": None, "total": {"$sum": "$amount"}}}
    ]
    result = await transactions.aggregate(pipeline).to_list(length=1)

    spent = result[0]["total"] if result else 0
    status = "Under Budget" if spent <= monthly_budget else "Over Budget"

    return web.json_response({
        "user_id": user_id,
        "budget": monthly_budget,
        "spent": spent,
        "status": status
    })
