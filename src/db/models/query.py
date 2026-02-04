from .base import Base
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from datetime import datetime
from sqlalchemy.orm import relationship


class Query(Base):
    __tablename__ = "queries"
    
    id = Column(Integer, primary_key=True, index=True)
    userid = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=True)
    cluster = Column(Integer, nullable=True)
    latency_ms = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relation avec l'utilisateur
    user = relationship("User", back_populates="queries")