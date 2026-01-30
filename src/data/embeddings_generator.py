from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma



def create_chroma_vectorstore(chunks):
    """
    Génère les embeddings des chunks
    et les stocke dans ChromaDB (persistée).
    """

    # 1. Modèle d'embeddings HuggingFace
    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # 2. Création de la base vectorielle
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory="data/chroma"
    )

    # 3. Persistance sur disque
    vectorstore.persist()

    return vectorstore


