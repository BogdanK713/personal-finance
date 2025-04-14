from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# User Service routes
@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        response = requests.get('http://user-service/api/users')
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return str(e), 500

@app.route('/api/users/register', methods=['POST'])
def register_user():
    try:
        response = requests.post('http://user-service/api/users/register', json=request.json)
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return str(e), 500

@app.route('/api/users/login', methods=['POST'])
def login_user():
    try:
        response = requests.post('http://user-service/api/users/login', json=request.json)
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return str(e), 500

# Transaction Service routes
@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    try:
        response = requests.get('http://transaction-service/api/transactions')
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return str(e), 500

# Analytics Service routes
@app.route('/api/analytics/summary', methods=['GET'])
def get_summary():
    try:
        response = requests.get('http://analytics-service/api/analytics/summary')
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
