# src/rag/prompt.py
from langchain_core.prompts import PromptTemplate

RAG_PROMPT = PromptTemplate(
    template="""You are an IT support assistant. Use the following context to answer the question.
If you don't know the answer, just say you don't know. Don't make up an answer.

Context: {context}

Question: {question}

Answer: """,
    input_variables=["context", "question"]
)

if __name__ == "__main__":
    print("✅ Prompt template chargé")
    print(f"📝 Variables: {RAG_PROMPT.input_variables}")