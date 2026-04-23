# 🔐 AI-Based Auth System (FastAPI Backend)

A secure authentication system built with **FastAPI**, featuring:

* JWT Authentication (Access + Refresh Tokens)
* Login History Tracking (IP, Location, Device)
* AI-based Suspicious Login Detection
* PostgreSQL Database Integration
* Token Refresh Mechanism

---

## 📁 Project Structure

```
backend/
│
├── app/
│   ├── routes/            # API routes (auth, user, ai)
│   ├── utils/             # Helper modules (security, AI logic)
│   ├── __pycache__/       # Python cache files
│   ├── models.py          # Database models
│   ├── schemas.py         # Pydantic schemas
│   ├── database.py        # DB connection setup
│   ├── config.py          # Environment config
│   └── main.py            # FastAPI entry point
│
├── venv/                  # Virtual environment
├── .env                   # Environment variables
├── requirements.txt       # Dependencies
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd backend
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```
SECRET_KEY=your_secret_key
ALGORITHM=HS256
DATABASE_URL=postgresql://user:password@localhost/dbname
```

---

## 🚀 Run Server

```bash
uvicorn app.main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

## 🔐 Authentication Flow

### ✅ Register

`POST /auth/register`

```json
{
  "email": "test@example.com",
  "password": "123456"
}
```

---

### ✅ Login

`POST /auth/login`

Returns:

* Access Token
* Refresh Token
* AI Security Result

---

### 🔄 Refresh Token

`POST /auth/refresh`

```json
{
  "token": "refresh_token_here"
}
```

---

## 👤 User APIs

### 🔒 Get Profile

`GET /user/profile`

### 📊 Login History

`GET /user/login-history`

Returns:

* IP Address
* City
* Latitude / Longitude
* Device info

---

## 🤖 AI Module

### Analyze Text

`POST /ai/analyze`

```json
{
  "text": "login attempt from new device"
}
```

Response:

* Normal activity OR
* Suspicious alert

---

## 🧠 Features

* 🌍 IP-based Location Tracking
* 📱 User-Agent Detection
* 🔐 Secure Password Hashing
* 🔄 Auto Token Refresh
* 🤖 Basic AI Threat Detection

---

## 🛠 Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* JWT (python-jose)
* Pydantic
* Requests

---

## ⚠️ Notes

* Make sure PostgreSQL is running
* Run migrations or recreate DB if schema changes
* `.env` file must be configured correctly

---

## 🚀 Future Improvements

* Role-based authentication
* Advanced AI anomaly detection
* Email alerts for suspicious logins
* Rate limiting & brute-force protection

---

## 👨‍💻 Author

Developed by **Hariom**
