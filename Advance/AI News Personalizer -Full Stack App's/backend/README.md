# 🧠 AI News Personalizer – Backend

FastAPI backend that fetches news articles and enhances them using AI-generated summaries and insights.

---

## 🚀 Features

* 📰 Fetch latest news (API integration)
* 🤖 AI-powered summarization
* 📌 “Why it matters” insights
* ⚡ FastAPI high-performance backend
* 🔌 REST API for frontend

---

## 🛠️ Tech Stack

* Python
* FastAPI
* Uvicorn
* Requests (or News API)
* OpenAI / LLM API (optional)

---

## 📁 Project Structure

```
backend/
 ├── app/
 │    ├── main.py
 │    ├── api/
 │    │    └── routes/
 │    │         └── news.py
 │    │
 │    ├── services/
 │    │    ├── news_service.py
 │    │    └── ai_service.py
 │    │
 │    ├── core/
 │    │    └── config.py
 │    │
 │    └── models/
 │
 ├── requirements.txt
 └── .env
```

---

## ⚙️ Setup Instructions

### 1. Clone repository

```
git clone <your-backend-repo-url>
cd backend
```

---

### 2. Create virtual environment

```
python -m venv venv
```

Activate:

**Windows:**

```
venv\Scripts\activate
```

**Mac/Linux:**

```
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Configure environment

Create `.env` file:

```
NEWS_API_KEY=your_api_key
OPENAI_API_KEY=your_openai_key
```

---

### 5. Run server

```
python -m uvicorn app.main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

## 🔗 API Endpoints

### Get News

```
GET /api/news/
```

### Response

```
{
  "results": [
    {
      "title": "...",
      "url": "...",
      "ai": "AI generated summary..."
    }
  ]
}
```

---

## 🌐 CORS Setup

Make sure this is added in `main.py`:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## ⚠️ Common Issues

### 307 Redirect

Use trailing slash:

```
/api/news/
```

### No articles found

Check API key validity.

---

## 🚀 Future Improvements

* Structured AI output (JSON format)
* User personalization
* Database integration
* Caching (Redis)

---

## 👨‍💻 Author

Hariom Verma
