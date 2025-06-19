from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON
from datetime import datetime
from app.models.base import Base

class CompanyConfig(Base):
    __tablename__ = "company_config"

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer, ForeignKey("companies.id"))
    whatsapp_number = Column(String(20))
    timezone = Column(String(50))
    language = Column(String(10))
    api = Column(JSON)  # {"api_key": "", "secret_id": ""}
    theme_id = Column(Integer, ForeignKey("theme.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
