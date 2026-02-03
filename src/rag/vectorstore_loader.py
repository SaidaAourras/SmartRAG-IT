# src/rag/vectorstore_loader.py
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


def load_vectorstore(persist_directory: str = "data/chroma"):
    """
    Charge le vectorstore ChromaDB
    Args:
        persist_directory: Chemin vers le dossier de persistence ChromaDB
    Returns:
        Instance de Chroma vectorstore
    """
    
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding_model
    )

    print(f" Vectorstore chargé depuis {persist_directory}")
    print(f" Nombre de documents : {vectorstore._collection.count()}")

    return vectorstore


if __name__ == "__main__":
    print(" Testing vectorstore loader...")
    try:
        vs = load_vectorstore()
        print(" Vectorstore loaded successfully!")
    except Exception as e:
        print(f" Error: {e}")