# 🧠 AI News Personalizer – Frontend

A React-based frontend for an AI-powered news application that delivers summarized, insightful, and personalized news content.

---

## 🚀 Features

* 📄 AI-generated news summaries
* 🧠 “Why it matters” insights
* 🔗 Direct link to full articles
* ⚡ Fast and responsive UI
* 🔌 Connected to FastAPI backend

---

## 🛠️ Tech Stack

* React (Create React App)
* Axios
* CSS (basic styling)

---

## 📁 Project Structure

```
src/
 ├── components/
 │    ├── Navbar.js
 │    ├── NewsCard.js
 │    ├── NewsList.js
 │    └── Loader.js
 │
 ├── pages/
 │    └── Home.js
 │
 ├── services/
 │    └── api.js
 │
 ├── App.js
 ├── index.js
 └── App.css
```

---

## ⚙️ Setup Instructions

### 1. Clone repository

```
git clone <your-frontend-repo-url>
cd frontend
```

### 2. Install dependencies

```
npm install
```

### 3. Configure environment

Create `.env` file:

```
REACT_APP_API_URL=http://localhost:8000/api
```

---

### 4. Run the app

```
npm start
```

App runs at:

```
http://localhost:3000
```

---

## 🔗 API Integration

Frontend connects to backend endpoint:

```
GET /api/news/
```

Expected response:

```
{
  "results": [
    {
      "title": "...",
      "url": "...",
      "ai": "AI generated summary text..."
    }
  ]
}
```

---

## ⚠️ Common Issues

### CORS Error

Make sure backend has CORS enabled.

### No news found

Ensure backend returns:

```
data.results
```

---

## 🚀 Future Improvements

* 🔍 Filters (category, tone)
* 🎯 Personalized feed
* 📊 Structured AI output (summary, bullets)
* ❤️ Bookmark feature

---

## 👨‍💻 Author

Hariom Verma
