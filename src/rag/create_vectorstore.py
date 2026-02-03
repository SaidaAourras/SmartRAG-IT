# src/rag/create_vectorstore.py
from pathlib import Path
from src.data.pdf_loader import load_pdf
from src.data.text_chunker import chunk_documents
from src.data.embeddings_generator import create_chroma_vectorstore

def main():
    print("🚀 Création du vectorstore")
    
    # 1. Charger le PDF
    pdf_path = "data/raw/data-pdf.pdf"
    
    if not Path(pdf_path).exists():
        print(f" ERREUR : Le fichier {pdf_path} n'existe pas")
        print(f" Veuillez placer votre fichier PDF dans : {pdf_path}")
        return
    
    print(f" Chargement de {pdf_path}...")
    documents = load_pdf(pdf_path)
    print(f" {len(documents)} pages chargées")
    
    # 2. Découper en chunks
    print("\n Découpage en chunks...")
    chunks = chunk_documents(documents, chunk_size=500, chunk_overlap=50)
    print(f" {len(chunks)} chunks créés")
    
    # 3. Créer le vectorstore
    print("\n Création des embeddings et du vectorstore...")
    vectorstore = create_chroma_vectorstore(chunks)
    
    print("\n Vectorstore créé avec succès !")
    print(f" {len(chunks)} chunks stockés dans data/chroma")
    print("\n Vous pouvez maintenant exécuter : python test_components.py")

if __name__ == "__main__":
    main()