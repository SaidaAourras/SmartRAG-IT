# src/rag/retriever.py

def create_retriever(vectorstore, k: int = 4):
    """
    Crée un retriever basé sur similarité vectorielle
    
    Args:
        vectorstore: Instance de Chroma vectorstore
        k: Nombre de documents à récupérer (par défaut: 4)
        
    Returns:
        Retriever configuré pour la recherche par similarité
    """
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )
    return retriever


if __name__ == "__main__":
    print(" Module retriever chargé avec succès")