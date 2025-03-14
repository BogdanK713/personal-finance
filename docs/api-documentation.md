# API Documentation

## User Service (Authentication)
- `POST /users/register` → Registers a new user
- `POST /users/login` → Authenticates user

## Transaction Service
- `POST /transactions/add` → Adds a transaction (income/expense)
- `GET /transactions/{user_id}` → Fetches user transactions

## Analytics Service
- `GET /analytics/summary` → Retrieves spending insights
