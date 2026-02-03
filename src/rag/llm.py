# src/rag/llm.py
import os
from dotenv import load_dotenv
from google import genai
from langchain_core.runnables import RunnableLambda

load_dotenv()


def load_llm():
    """
    Charge le LLM Gemini sous forme de fonction LangChain
    """
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY non trouvé dans .env")

    client = genai.Client(api_key=api_key)

    def gemini_call(prompt: str) -> str:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text

    # RunnableLangChain compatible LCEL
    return RunnableLambda(gemini_call)
