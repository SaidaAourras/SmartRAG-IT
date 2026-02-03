# src/rag/rag_chain.py

def build_rag_chain(llm, retriever, prompt_template):
    """
    Construit une chaîne RAG simple
    
    Args:
        llm: Le modèle de langage
        retriever: Le retriever pour chercher les documents
        prompt_template: Le template de prompt
        
    Returns:
        Une fonction qui prend une query et retourne la réponse
    """
    
    def rag_chain(input_dict):
        # 1. Récupérer la question
        question = input_dict.get("query", "")
        
        # 2. Chercher les documents pertinents
        docs = retriever.invoke(question)
        
        # 3. Formater le contexte
        context = "\n\n".join([doc.page_content for doc in docs])
        
        # 4. Créer le prompt complet
        full_prompt = prompt_template.format(
            context=context,
            question=question
        )
        
        # 5. Générer la réponse avec le LLM
        answer = llm.invoke(full_prompt)
        
        # 6. Retourner le résultat avec les sources
        return {
            "result": answer,
            "source_documents": docs
        }
    
    return rag_chain


if __name__ == "__main__":
    print("✅ Module rag_chain chargé avec succès")