# analytics_service/handlers/analytics.py
from aiohttp import web
from .db import get_collection


async def get_summary(request):
    transactions = get_collection("transactions")
    user_id = request.query.get("user_id")
    if not user_id:
        return web.json_response({"error": "Missing user_id"}, status=400)

    total = await transactions.count_documents({"user_id": user_id})
    return web.json_response({"total_transactions": total})


async def get_monthly(request):
    transactions = get_collection("transactions")
    user_id = request.query.get("user_id")
    if not user_id:
        return web.json_response({"error": "Missing user_id"}, status=400)

    pipeline = [
        {"$match": {"user_id": user_id}},
        {"$group": {
            "_id": {"month": {"$substr": ["$date", 0, 7]}},
            "total_income": {"$sum": {"$cond": [{"$eq": ["$type", "Income"]}, "$amount", 0]}},
            "total_expense": {"$sum": {"$cond": [{"$eq": ["$type", "Expense"]}, "$amount", 0]}}
        }},
        {"$sort": {"_id.month": 1}}
    ]
    result = await transactions.aggregate(pipeline).to_list(length=100)
    formatted = [{
        "month": r["_id"]["month"],
        "total_income": r["total_income"],
        "total_expense": r["total_expense"]
    } for r in result]

    return web.json_response({"data": formatted})


async def get_budget(request):
    transactions = get_collection("transactions")
    user_id = request.query.get("user_id")
    if not user_id:
        return web.json_response({"error": "Missing user_id"}, status=400)

    monthly_budget = 500  # Example static budget

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
