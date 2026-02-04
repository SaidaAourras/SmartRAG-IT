from src.rag.test_components import test_imports, test_vectorstore, test_retriever, test_llm, test_rag_chain
from src.services.ml_services import predict_cluster
from src.services.mlflow_service import log_rag_query
from datetime import datetime
import time

def rag_function(question, user_id):
    """
    Fonction principale du pipeline RAG avec tracking MLflow
    """
    start_time = time.time()
    
    # Imports et chargement du vectorstore
    test_imports()
    vectorstore = test_vectorstore()
    
    # Nettoyer la question
    user_query = question.strip()
    if not user_query:
        user_query = "What is the most basic principle of IT support?"
    
    # ✅ CORRECTION ICI : enlever k=4
    retriever = test_retriever(vectorstore, user_query)
    
    llm = test_llm()
    result = test_rag_chain(llm, retriever, user_query)
    
    # Prédiction du cluster
    predicted_cluster = predict_cluster(user_query)
    
    # Calcul de la latence
    end_time = time.time()
    latency_ms = (end_time - start_time) * 1000
    
    # Extraire la réponse et les chunks
    answer = result.get('result', '') if isinstance(result, dict) else str(result)
    source_documents = result.get('source_documents', []) if isinstance(result, dict) else []
    
    # Extraire les chunks et scores
    retrieved_chunks = [doc.page_content for doc in source_documents]
    similarity_scores = [
        doc.metadata.get('score', 0.0) 
        for doc in source_documents 
        if hasattr(doc, 'metadata')
    ]
    
    # Logger dans MLflow
    log_rag_query(
        question=user_query,
        answer=answer,
        cluster=predicted_cluster,
        latency_ms=latency_ms,
        user_id=user_id,
        retrieved_chunks=retrieved_chunks,
        similarity_scores=similarity_scores if similarity_scores else None
    )
    
    # Retourner les données
    return {
        'userid': user_id,
        'question': user_query,
        'answer': answer,
        'cluster': predicted_cluster,
        'latency_ms': round(latency_ms, 2),
        'created_at': datetime.utcnow()
    }


if __name__ == "__main__":
    result = rag_function(
        question="How did the author's early experience as a tinkerer lead to his career in IT support",
        user_id=1  
    )
    print("\n📋 Résultat du pipeline RAG:")
    print(f"Question: {result['question']}")
    print(f"Cluster: {result['cluster']}")
    print(f"Latence: {result['latency_ms']} ms")
    print(f"Réponse: {result['answer'][:200]}...")