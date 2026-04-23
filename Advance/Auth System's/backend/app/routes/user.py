from fastapi import APIRouter, Depends
from app.utils.dependencies import get_current_user
from app.database import SessionLocal
from app.models import LoginHistory


router = APIRouter()

@router.get("/profile")
def get_profile(user=Depends(get_current_user)):
    return {
        "message": "Protected route working",
        "user": user
    }


@router.get("/login-history")
def get_login_history(user=Depends(get_current_user)):
    db = SessionLocal()

    history = db.query(LoginHistory).filter(LoginHistory.email == user).all()

    return history