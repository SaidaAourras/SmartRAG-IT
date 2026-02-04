from .base import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from datetime import datetime
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)  # Ajout
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    isactive = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    queries = relationship("Query", back_populates="user", cascade="all, delete-orphan")