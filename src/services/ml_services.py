import numpy as np
import joblib
from langchain_huggingface import HuggingFaceEmbeddings
import os

pca_path = "ml/models/pca_model.joblib"
kmeans_path = "ml/models/kmeans_model.joblib"

# Vérifier que les fichiers existent
if not os.path.exists(pca_path):
    raise FileNotFoundError(f"❌ Modèle PCA introuvable : {pca_path}")
if not os.path.exists(kmeans_path):
    raise FileNotFoundError(f"❌ Modèle KMeans introuvable : {kmeans_path}")

pca = joblib.load(pca_path)
kmeans_model = joblib.load(kmeans_path)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def predict_cluster(question: str) -> int:
    
    try:
        
        question_embedding = embedding_model.embed_documents([question])
        question_embedding = np.array(question_embedding)
        
        # Réduire la dimensionnalité avec PCA
        question_pca = pca.transform(question_embedding)
        
        # Prédire le cluster
        cluster = kmeans_model.predict(question_pca)[0]
        
        print(f"📊 Question assignée au cluster: {cluster}")
        
        return int(cluster)
        
    except Exception as e:
        print(f"⚠️ Erreur lors de la prédiction du cluster: {e}")
        return 0