# 💰 Personal Finance Tracker

## 📌 Project Overview
The **Personal Finance Tracker** is a microservices-based system designed to help users manage their **income, expenses, and financial insights** efficiently.  
Built with **Clean Architecture**, it ensures loose coupling between services and scalability. The system follows **REST API** communication between services.

## 🛠️ Features
✔ **User Authentication** – Secure login & registration.  
✔ **Income & Expense Tracking** – Users can add, edit, and delete transactions.  
✔ **Financial Insights** – View spending summaries and monthly analytics.  
✔ **Multi-Currency Support** – Track expenses in different currencies.  
✔ **Budget Management** – Set limits and get alerts on overspending.  

## 🔗 Tech Stack
✔ **Backend:** FastAPI (User), Flask (Transactions), Django REST (Analytics)  
✔ **Database:** PostgreSQL (Users & Transactions), MongoDB (Analytics)  
✔ **Frontend:** React.js  
✔ **Security:** JWT Authentication  
✔ **Containerization:** Docker & Docker Compose    

## 🏗️ System Architecture

The system consists of the following services:
1. **User Service** – Handles authentication and user account management.
2. **Transaction Service** – Manages user transactions (income, expenses, categories).
3. **Analytics Service** – Processes financial data and provides spending insights.
4. **Web App** – A frontend interface for users to interact with the system.


## 🔗 API Communication
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
