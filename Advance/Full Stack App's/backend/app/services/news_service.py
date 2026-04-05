import requests
from app.core.config import NEWS_API_KEY

def fetch_news(query="technology"):
    try:
        url = f"https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        data = response.json()

        articles = data.get("articles", [])

        return [
            {
                "title": a.get("title"),
                "description": a.get("description") or "No description",
                "url": a.get("url"),
            }
            for a in articles[:5]
        ]

    except Exception as e:
        return []