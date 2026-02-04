from pydantic import BaseModel
from datetime import datetime

class QueryCreate(BaseModel):
    question : str
    

class QueryResponse(BaseModel):
    id: int
    question: str
    answer: str
    cluster: int
    latency_ms: float
    created_at: datetime
    
    
class QueryHistory(BaseModel):
    id: int
    question: str
    answer: str
    cluster: int
    created_at: datetime
    