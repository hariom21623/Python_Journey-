from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from app.utils.security import hash_password, verify_password
from app.auth import create_access_token
from fastapi import Request
from app.models import LoginHistory
from app.utils.ai_module import detect_suspicious_login

import requests
from datetime import datetime, timedelta
from jose import jwt
from app.config import settings


router = APIRouter()

def get_location(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}")
        data = res.json()
        return {
            "city": data.get("city"),
            "lat": data.get("lat"),
            "lon": data.get("lon"),
        }
    except:
        return None

def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=7)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing = db.query(models.User).filter(models.User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = models.User(
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"msg": "User created"}


@router.post("/login")
def login(user: schemas.UserLogin, request: Request, db: Session = Depends(get_db)):

    db_user = db.query(models.User).filter(models.User.email == user.email).first()

    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # 🌍 Get location
    ip = request.client.host
    location = get_location(ip)

    # 🤖 AI detection
    ai_result = detect_suspicious_login(
        ip=ip,
        user_agent=request.headers.get("user-agent", "")
    )

    # 🕵️ Save login history
    login_record = LoginHistory(
        email=user.email,
        ip_address=ip,
        user_agent=request.headers.get("user-agent"),
        city=location.get("city") if location else None,
        lat=location.get("lat") if location else None,
        lon=location.get("lon") if location else None,
    )

    db.add(login_record)
    db.commit()

    # 🔐 Tokens
    access_token = create_access_token({"sub": db_user.email})
    refresh_token = create_refresh_token({"sub": db_user.email})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
        "ai_security": ai_result or {}
    }

    return {"access_token": token, "token_type": "bearer"}

@router.post("/refresh")
def refresh_token_api(data: dict):
    token = data.get("token")

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email = payload.get("sub")

        new_access = create_access_token({"sub": email})

        return {"access_token": new_access}
    except:
        raise HTTPException(status_code=401, detail="Invalid refresh token")