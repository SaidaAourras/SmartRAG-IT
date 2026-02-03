from langchain_text_splitters import RecursiveCharacterTextSplitter
# from src.data.embeddings_generator import create_chroma_vectorstore

def chunk_documents(documents, chunk_size=500, chunk_overlap=50):
    """
    Découpe les documents en chunks pour le RAG
    
    Args:
        documents: Liste de documents LangChain
        chunk_size: Taille des chunks en caractères
        chunk_overlap: Chevauchement entre chunks
        
    Returns:
        Liste de chunks
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    
    chunks = text_splitter.split_documents(documents)
    print(f"✅ {len(documents)} documents découpés en {len(chunks)} chunks")
    
    return chunks


