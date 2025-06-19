from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.base import Base

class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String(150))
    email = Column(String(100), unique=True)
    responsible_name = Column(String(100))
    responsible_email = Column(String(100))
    cnpj_cpf = Column(String(30))
    password_hash = Column(String)
    password_hash_confirm = Column(String)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
