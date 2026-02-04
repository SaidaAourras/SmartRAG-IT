"""
Service MLflow simple pour tracking RAG
"""
import mlflow
import os
from datetime import datetime
from typing import Dict, Any, List

# Configuration MLflow
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI", "sqlite:///mlflow.db")
EXPERIMENT_NAME = "RAG_IT_Support"

# Initialiser MLflow une seule fois
mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

try:
    mlflow.set_experiment(EXPERIMENT_NAME)
    print(f"✅ Expérience MLflow configurée: {EXPERIMENT_NAME}")
except Exception as e:
    print(f"⚠️ Erreur configuration MLflow: {e}")


def log_rag_query(
    question: str,
    answer: str,
    cluster: int,
    latency_ms: float,
    user_id: int,
    retrieved_chunks: List[str] = None,
    similarity_scores: List[float] = None
):
    """
    Enregistre une requête RAG dans MLflow
    
    Args:
        question: Question de l'utilisateur
        answer: Réponse générée
        cluster: Cluster prédit
        latency_ms: Temps de traitement
        user_id: ID utilisateur
        retrieved_chunks: Documents récupérés (optionnel)
        similarity_scores: Scores de similarité (optionnel)
    """
    try:
        # Créer un nom de run unique
        run_name = f"query_user{user_id}_{datetime.now().strftime('%H%M%S')}"
        
        with mlflow.start_run(run_name=run_name):
            
            # === PARAMÈTRES ===
            mlflow.log_param("user_id", user_id)
            mlflow.log_param("cluster", cluster)
            mlflow.log_param("question_length", len(question))
            
            # Configuration RAG (à ajuster selon votre config)
            mlflow.log_param("model", "gemini-2.0-flash-exp")
            mlflow.log_param("temperature", 0.7)
            mlflow.log_param("k_documents", 4)
            
            # === MÉTRIQUES ===
            mlflow.log_metric("latency_ms", latency_ms)
            mlflow.log_metric("answer_length", len(answer))
            mlflow.log_metric("answer_word_count", len(answer.split()))
            
            # Scores de similarité si disponibles
            if similarity_scores:
                avg_score = sum(similarity_scores) / len(similarity_scores)
                mlflow.log_metric("avg_similarity_score", avg_score)
                mlflow.log_metric("min_similarity_score", min(similarity_scores))
                mlflow.log_metric("max_similarity_score", max(similarity_scores))
            
            # === TAGS ===
            mlflow.set_tag("environment", os.getenv("ENVIRONMENT", "development"))
            mlflow.set_tag("pipeline", "RAG")
            
            # === ARTIFACTS (fichiers texte) ===
            # Sauvegarder la question
            question_file = f"temp_question_{user_id}.txt"
            with open(question_file, "w", encoding="utf-8") as f:
                f.write(question)
            mlflow.log_artifact(question_file, "inputs")
            os.remove(question_file)
            
            # Sauvegarder la réponse
            answer_file = f"temp_answer_{user_id}.txt"
            with open(answer_file, "w", encoding="utf-8") as f:
                f.write(answer)
            mlflow.log_artifact(answer_file, "outputs")
            os.remove(answer_file)
            
            # Sauvegarder les chunks si disponibles
            if retrieved_chunks:
                chunks_file = f"temp_chunks_{user_id}.txt"
                with open(chunks_file, "w", encoding="utf-8") as f:
                    for i, chunk in enumerate(retrieved_chunks, 1):
                        f.write(f"=== Chunk {i} ===\n{chunk}\n\n")
                mlflow.log_artifact(chunks_file, "retrieved_data")
                os.remove(chunks_file)
            
            print(f"✅ MLflow: Requête loggée pour user {user_id}")
            
    except Exception as e:
        print(f"⚠️ Erreur MLflow logging: {e}")