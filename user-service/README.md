# 🛠️ User Service - Personal Finance Tracker

## 📌 Overview
The **User Service** handles user authentication, registration, and profile management in the **Personal Finance Tracker**.  
It ensures **secure login, JWT authentication, and user profile updates**.

## 🔗 API Endpoints

| Method | Endpoint           | Description                |
|--------|-------------------|----------------------------|
| POST   | `/users/register` | Register a new user        |
| POST   | `/users/login`    | Authenticate user & return JWT |
| GET    | `/users/profile`  | Retrieve logged-in user profile |
| PATCH  | `/users/update`   | Update user profile details |
| DELETE | `/users/delete`   | Delete user account |

## 🏗️ Tech Stack
✔ **Backend:** FastAPI (Python)  
✔ **Database:** PostgreSQL  
✔ **Security:** JWT Authentication, bcrypt  
✔ **Communication:** REST API  

## 🔐 Features
✔ **User Registration & Login**  
✔ **Secure Password Storage (bcrypt)**  
✔ **JWT-Based Authentication** 