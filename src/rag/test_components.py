# src/rag/test_components.py
import sys
import warnings

# Supprimer les avertissements de dépréciation pour un output plus propre
warnings.filterwarnings("ignore", category=UserWarning)

def test_imports():
    try:
        from langchain_huggingface import HuggingFaceEmbeddings
        from langchain_chroma import Chroma
        from google import genai
        from langchain_core.language_models.llms import LLM
        print(" Tous les modules sont installés")
    except Exception as e:
        print(f" ERREUR d'import: {e}")
        sys.exit(1)


def test_vectorstore():
    from src.rag.vectorstore_loader import load_vectorstore
    try:
        vectorstore = load_vectorstore()
        return vectorstore
    
    except Exception as e:
        print(f" ERREUR Vectorstore: {e}")
        sys.exit(1)


def test_retriever(vectorstore, query):

    from src.rag.retriever import create_retriever
    
    retriever = create_retriever(vectorstore, k=4)
    # docs = retriever.invoke(query)
    
    print(f" Recherche effectuée pour : '{query}'")
    
    return retriever

def test_llm():

    from src.rag.llm import load_llm
    try:
        llm = load_llm()
        
        print(" LLM prêt")
        return llm
    except Exception as e:
        print(f" ERREUR LLM: {e}")
        print("💡 Vérifiez que GEMINI_API_KEY est défini dans votre .env")
        sys.exit(1)



def test_rag_chain(llm, retriever, question):
   
    from src.rag.prompt import RAG_PROMPT
    from src.rag.rag_chain import build_rag_chain
    
    try:
        # Construire la chaîne RAG
        rag_chain = build_rag_chain(llm, retriever, RAG_PROMPT)
        
        print(f"🤔 L'IA réfléchit à : {question}...")
        
        # Invoquer la chaîne RAG
        result = rag_chain({"query": question})
        
        # print("\n✨ RÉPONSE :")
        # print("-" * 60)
        # print(result["result"])
        # print("-" * 60)
        
        return result
        
        # Afficher les sources utilisées
        # print(f"\n Sources utilisées : {len(result['source_documents'])} documents")
        
    except Exception as e:
        print(f" ERREUR dans la chaîne RAG: {e}")
        import traceback
        traceback.print_exc()

def main():
    print("\n SYSTÈME RAG - TEST INTERACTIF\n")
    
    test_imports()
    vectorstore = test_vectorstore()
    
    # Demander la question dès le début
    user_query = input("\n❓ Entrez votre question de test : ").strip()
    if not user_query:
        user_query = "What is the most basic principle of IT support?"
        print(f"   (Question par défaut utilisée : {user_query})")

    retriever = test_retriever(vectorstore, user_query)
    llm = test_llm()
    test_rag_chain(llm, retriever, user_query)
    
    print("\n" + "="*60)
    print("✅ FIN DES TESTS")
    print("="*60)

if __name__ == "__main__":
    main()