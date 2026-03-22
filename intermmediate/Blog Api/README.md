# 📝 Flask Blog API (PostgreSQL)

    A simple and scalable RESTful Blog API built using **Flask**, **SQLAlchemy**, and **PostgreSQL**.  
    This project demonstrates clean architecture, CRUD operations, and real-world backend structure.

---

## 🚀 Features

    - Create blog posts
    - Get all posts
    - Get single post
    - Update post
    - Delete post
    - PostgreSQL database integration
    - Clean project structure (modular Flask app)

---

## 🏗️ Project Structure
    blog_api/
    │
    ├── app/
    │ ├── init.py # App factory
    │ ├── routes.py # API routes
    │ ├── models.py # Database models
    │ ├── database.py # DB initialization
    │
    ├── run.py # Entry point
    ├── config.py # Configuration
    ├── requirements.txt # Dependencies


---

## ⚙️ Installation

### 1. Clone the repository
    git clone https://github.com/your-username/blog-api.git
    cd blog-api

### 2. Create virtual environment

python -m venv venv
venv\Scripts\activate # Windows


### 3. Install dependencies

pip install -r requirements.txt


---

## 🗄️ PostgreSQL Setup

### Create database

    CREATE DATABASE blogdb;


### Update config

    Edit `config.py`:
    SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost:5432/blogdb"

---

## ▶️ Run the Application

    python run.py

    Server will start at:

    http://127.0.0.1:5000

---

## 📌 API Endpoints

### 🔹 Create Post
**POST** `/posts`

    {
    "title": "My First Post",
    "content": "Hello World"
    }
---

### 🔹 Get All Posts
**GET** `/list`

---

### 🔹 Get Single Post
**GET** `/list/<id>`

---

### 🔹 Update Post
**PUT** `/update/<id>`

    {
    "title": "Updated Title",
    "content": "Updated Content"
    }

---

### 🔹 Delete Post
**DELETE** `/delete/<id>`

---

## 🧠 Tech Stack

    - Python
    - Flask
    - Flask-SQLAlchemy
    - PostgreSQL
    - REST API

---

## 📈 Future Improvements

    - User authentication (JWT)
    - User model & relationships
    - Pagination
    - Search functionality
    - Docker support
    - Deployment (Render / AWS)

---

## ⚠️ Notes

    - This project uses Flask development server (not for production)
    - Use environment variables for database credentials in production

---

## 👨‍💻 Author

    Hariom Verma
    Learning Backend Development 🚀

---