from langchain.text_splitter import RecursiveCharacterTextSplitter
from src.data.pdf_loader import docs

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    length_function=len,
    separators=["\n\n", "\n", " ", ""]
)

chunks = text_splitter.split_documents(docs)

print(f"Nombre de chunks créés : {len(chunks)}")

# 4. Examiner un chunk
print("\n--- Exemple de chunk ---")
print(chunks[0])
print(f"Contenu : {chunks[0].page_content}...")
print(f"Métadonnées : {chunks[0].metadata}")