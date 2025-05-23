from flask import Flask, jsonify, request
from flask_cors import CORS
import grpc
import transaction_pb2 as pb2
import transaction_pb2_grpc as pb2_grpc
import requests

app = Flask(__name__)
CORS(app)  # ✅ Enable CORS for all routes

# --- gRPC Setup ---
def get_grpc_stub():
    channel = grpc.insecure_channel("transaction-service:50051")
    return pb2_grpc.TransactionServiceStub(channel)

# --- User Service Routes ---
@app.route('/api/users/register', methods=['POST'])
def register_user():
    try:
        response = requests.post("http://user-service:8000/users/register", json=request.json)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/users/login', methods=['POST'])
def login_user():
    try:
        response = requests.post("http://user-service:8000/users/login", json=request.json)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

# --- Analytics Service Routes ---
@app.route('/api/analytics/summary', methods=['GET'])
def analytics_summary():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing user_id parameter"}), 400
    try:
        response = requests.get(f"http://analytics-service:8002/analytics/summary?user_id={user_id}")
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/analytics/monthly', methods=['GET'])
def analytics_monthly():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing user_id parameter"}), 400
    try:
        response = requests.get(f"http://analytics-service:8002/analytics/monthly?user_id={user_id}")
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/analytics/budget', methods=['GET'])
def analytics_budget():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing user_id parameter"}), 400
    try:
        response = requests.get(f"http://analytics-service:8002/analytics/budget?user_id={user_id}")
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

# --- Transaction Service Routes ---
@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    stub = get_grpc_stub()
    user_id = request.args.get("user_id", "")
    response = stub.GetTransactions(pb2.TransactionRequest(user_id=user_id))
    return jsonify([{
        "id": txn.id,
        "category": txn.category,
        "amount": txn.amount,
        "type": txn.type,
        "date": txn.date
    } for txn in response.transactions])

@app.route('/api/transactions', methods=['POST'])
def add_transaction():
    stub = get_grpc_stub()
    data = request.json
    grpc_req = pb2.TransactionRequest(
        user_id=data["user_id"],
        category=data["category"],
        amount=data["amount"],
        type=data["type"],
        date=data["date"]
    )
    response = stub.AddTransaction(grpc_req)
    return jsonify({"status": response.status, "message": response.message})

# --- Run ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
