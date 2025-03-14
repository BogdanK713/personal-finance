# Personal Finance Tracker 💰📊

## 📌 Project Overview
The **Personal Finance Tracker** is a microservices-based system designed to help users manage their income, expenses, and financial insights efficiently.  
This system is built using **Clean Architecture** principles and consists of multiple independent microservices that communicate via REST APIs.

## 🛠️ System Architecture
The system consists of the following services:
1. **User Service** – Handles authentication and user account management.
2. **Transaction Service** – Manages user transactions (income, expenses, categories).
3. **Analytics Service** – Processes financial data and provides spending insights.
4. **Web App** – A frontend interface for users to interact with the system.

## 🔗 API Communication
All microservices communicate using **REST APIs**.
- `POST /users/register` → Register a new user.
- `POST /transactions/add` → Add a financial transaction.
- `GET /analytics/summary` → Retrieve spending insights.

## 📂 Repository Structure
```bash
/personal-finance-tracker
│── /user-service             # User authentication & profiles  
│── /transaction-service      # Income & expense tracking  
│── /analytics-service        # Spending insights & reports  
│── /web-app                  # Frontend UI  
│── /docs                     # Architecture diagrams, API documentation  
│── docker-compose.yml        # Manages service orchestration  
│── README.md                 # Project overview  
```
## 🚀 Getting Started

# Clone the repository
git clone https://github.com/BogdanK713/personal-finance-tracker.git
