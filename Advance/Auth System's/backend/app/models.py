from sqlalchemy import Column, Integer, String, DateTime,Float, ForeignKey
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

class LoginHistory(Base):
    __tablename__ = "login_history"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    ip_address = Column(String)
    user_agent = Column(String)
    city = Column(String)
    lat = Column(Float)
    lon = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)