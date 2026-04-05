import requests
import json
from app.core.config import GOOGLE_API_KEY

def process_article(article: dict, level: str = "normal"):
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GOOGLE_API_KEY}"

        # ✅ Fix: extract text properly
        article_text = article.get("description") or article.get("content") or article.get("title")

        prompt = f"""
            Analyze the following news article and return STRICT JSON format:

            Article:
            {article_text}

            Return JSON like this:

            {{
            "summary": "short summary",
            "bullet_points": ["point1", "point2", "point3"],
            "why_it_matters": "why important",
            "tone": "tone of article"
            }}

            ONLY return JSON. No explanation.
            """

        payload = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ]
        }

        response = requests.post(url, json=payload)
        data = response.json()

        if "candidates" not in data:
            return {
                "summary": "Error generating AI",
                "bullet_points": [],
                "why_it_matters": "",
                "tone": ""
            }

        # ✅ Extract text
        ai_text = data["candidates"][0]["content"]["parts"][0]["text"]

        # ✅ Clean response (important for Gemini sometimes adds ```json)
        ai_text = ai_text.replace("```json", "").replace("```", "").strip()

        # ✅ Convert to JSON
        try:
            ai_json = json.loads(ai_text)
        except:
            ai_json = {
                "summary": ai_text,
                "bullet_points": [],
                "why_it_matters": "",
                "tone": ""
            }

        return ai_json

    except Exception as e:
        return {
            "summary": f"AI Error: {str(e)}",
            "bullet_points": [],
            "why_it_matters": "",
            "tone": ""
        }