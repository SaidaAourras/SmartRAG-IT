from src.rag.test_components import test_imports, test_vectorstore, test_retriever, test_llm, test_rag_chain
from src.services.ml_services import predict_cluster  
from datetime import datetime
import time

def rag_function(question, user_id):
    
    start_time = time.time()

    test_imports()
    vectorstore = test_vectorstore()

    user_query = question.strip()
    if not user_query:
        user_query = "What is the most basic principle of IT support?"
   
    retriever = test_retriever(vectorstore, user_query)
    llm = test_llm()
    result = test_rag_chain(llm, retriever, user_query)

    predicted_cluster = predict_cluster(user_query)

    end_time = time.time()
    latency_ms = (end_time - start_time) * 1000
    
    answer = result.get('result', '') if isinstance(result, dict) else str(result)
    
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
