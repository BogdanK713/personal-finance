# 📊 Analytics Service

## 📌 Overview
The **Analytics Service** provides **spending insights, budget reports, and financial summaries** for users.

## 🔗 API Endpoints
| Method | Endpoint               | Description |
|--------|------------------------|-------------|
| GET    | `/analytics/summary`   | Retrieve a spending summary |
| GET    | `/analytics/monthly`   | Get monthly expense breakdown |
| GET    | `/analytics/budget`    | Check budget compliance |

## 🏗️ Tech Stack
✔ **Backend:** Django REST Framework (Python)  
✔ **Database:** MongoDB  
✔ **Security:** JWT Authentication 

## 🔢 Data Flow
- **Pulls transaction data** from the `Transaction Service`
- **Processes insights** (e.g., **total expenses, category distribution**)
- **Returns insights to the frontend**  

## 📈 Features
✔ Monthly spending trends  
✔ Savings recommendations  
✔ Budget tracking  
