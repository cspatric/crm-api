from sqlalchemy import Column, Integer, String, JSON, DateTime
from datetime import datetime
from app.models.base import Base

class Theme(Base):
    __tablename__ = "theme"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    color_palette = Column(JSON)  # {"color1": "#fff", "color2": "#000", ...}
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
