from fastapi import APIRouter
from app.services.news_service import fetch_news
from app.services.ai_service import process_article

router = APIRouter()

@router.get("/")
def get_ai_news(query: str = "technology", level: str = "normal"):
    articles = fetch_news(query)

    if not articles:
        return {"error": "No articles found. Check API key."}

    results = []
    for article in articles:
        ai_output = process_article(article, level)

        results.append({
        "title": article["title"],
        "url": article["url"],
        "ai": process_article(article)
    })

    return {"results": results}