from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.db.schemas.query import QueryCreate, QueryResponse
from ..dependencies import get_db
from src.services.auth_services import verify_token
from src.db.models.query import Query 
from src.rag.pipeline_rag import rag_function

query_router = APIRouter(prefix='/queries', tags=["queries"])


@query_router.post('/ask', response_model=QueryResponse)
def ask_question(
    query_data: QueryCreate,
    db: Session = Depends(get_db),
    current_user_data: dict = Depends(verify_token)
):
   
    try:
        user_id = current_user_data.get("id") or current_user_data.get("sub")
        
        if not user_id:
            raise HTTPException(
                status_code=401,
                detail="ID utilisateur introuvable dans le token"
            )
        
        user_id = int(user_id)
        question_text = query_data.question
        
        # ⭐ Le tracking MLflow se fait automatiquement ici
        rag_result = rag_function(question_text, user_id)
        
        # Sauvegarder dans PostgreSQL
        db_query = Query(**rag_result)
        db.add(db_query)
        db.commit()
        db.refresh(db_query)
        
        return db_query
        
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Erreur lors du traitement de la question: {str(e)}"
        )