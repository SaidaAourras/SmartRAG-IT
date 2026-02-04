
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.db.schemas.query import  QueryHistory
from ..dependencies import get_db
from src.services.auth_services import verify_token
from src.db.models.query import Query 

query_history_router = APIRouter(prefix='/queries', tags=["queries"])

@query_history_router.get('/history', response_model=List[QueryHistory])
def get_user_history(
    limit: int = 50,
    offset: int = 0,
    db: Session = Depends(get_db),
    current_user_data: dict = Depends(verify_token)
):
   
    try:
        # Récupérer l'ID utilisateur
        user_id = current_user_data.get("id") or current_user_data.get("sub")
        
        if not user_id:
            raise HTTPException( status_code=401, detail="ID utilisateur introuvable dans le token")
        
        user_id = int(user_id)
        if limit > 100:
            limit = 100

        queries = db.query(Query)\
            .filter(Query.userid == user_id)\
            .order_by(Query.created_at.desc())\
            .offset(offset)\
            .limit(limit)\
            .all()
        
        return queries
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erreur lors de la récupération de l'historique: {str(e)}"
        )