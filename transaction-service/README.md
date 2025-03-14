# 💵 Transaction Service

## 📌 Overview
The **Transaction Service** allows users to **track their income and expenses** by storing financial transactions.

## 🔗 API Endpoints
| Method | Endpoint                   | Description |
|--------|----------------------------|-------------|
| POST   | `/transactions/add`        | Add a new transaction |
| GET    | `/transactions/{user_id}`  | Fetch all user transactions |
| PATCH  | `/transactions/update/{id}` | Modify a transaction |
| DELETE | `/transactions/delete/{id}` | Remove a transaction |

## 🏗️ Tech Stack
✔ **Backend:** Flask (Python)  
✔ **Database:** PostgreSQL  
✔ **Security:** JWT Authentication 

## 📊 Transaction Categories
- **Income:** Salary, Freelancing, Investments  
- **Expenses:** Food, Rent, Transportation, Entertainment  

## 🛠️ Future Enhancements
✔ Recurring transactions  
✔ AI-based expense prediction  
✔ Budget alerts  
