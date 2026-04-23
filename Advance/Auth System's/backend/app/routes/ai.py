from fastapi import APIRouter

router = APIRouter()

@router.post("/analyze")
def analyze(data: dict):
    text = data.get("text", "")
    if not text:
        return {"error": "No text provided"}

    if "hack" in text.lower():
        return {"alert": "Suspicious activity detected"}

    return {"message": "Normal activity"}