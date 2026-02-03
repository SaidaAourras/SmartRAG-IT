# src/data/pdf_loader.py
from langchain_community.document_loaders import PyPDFLoader

def load_pdf(pdf_path):
    """
    Charge un PDF et retourne les documents
    
    Args:
        pdf_path: Chemin vers le fichier PDF
        
    Returns:
        Liste de documents LangChain
    """
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    
    print(f"✅ PDF chargé : {len(documents)} pages")
    
    return documents 


if __name__ == "__main__":
    # Test
    docs = load_pdf('data/raw/data-pdf.pdf')
    
    if docs:
        print(f"\n📊 Informations :")
        print(f"Nombre de pages : {len(docs)}")
        print(f"\nPremière page :")
        print(f"Contenu : {docs[0].page_content[:200]}...")
        print(f"Métadonnées : {docs[0].metadata}")
    else:
        print("❌ Aucun document chargé")