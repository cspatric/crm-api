from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from datetime import datetime
from app.models.base import Base

class Agent(Base):
    __tablename__ = "agents"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    company_id = Column(Integer, ForeignKey("companies.id"))
    email = Column(String(100))
    profile_picture = Column(String)
    bio = Column(String)
    role_id = Column(Integer, ForeignKey("roles.id"))
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
