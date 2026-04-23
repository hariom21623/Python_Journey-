def analyze_text(text: str):
    if "error" in text.lower():
        return {"risk": "HIGH", "message": "Possible issue detected"}
    return {"risk": "LOW", "message": "Looks safe"}


def detect_suspicious_login(ip: str, user_agent: str):
    risk = "LOW"

    if "bot" in user_agent.lower():
        risk = "HIGH"

    if ip.startswith("192.168"):
        risk = "MEDIUM"

    return {
        "risk": risk,
        "message": "Suspicious login detected" if risk != "LOW" else "Normal login"
    }