from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
import os
from sentence_transformers import SentenceTransformer

DB_DIR = "vectorDB"
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
# embedding_model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")

def save_vector_store(chunks):
    db = FAISS.from_documents(documents=chunks, embedding=embedding_model)
    db.save_local(DB_DIR)
    print("✅ 5. Save vectorDB to local memory successfully.\n")


    
def load_vector_store():
    if not os.path.exists(DB_DIR):
        raise FileNotFoundError("Vector store not found. Please run embedding step first.")

    return FAISS.load_local(DB_DIR, embedding_model, allow_dangerous_deserialization=True)


def search_context(query, k=3):
    db = load_vector_store()
    docs = db.similarity_search(query, k=k)
    return "\n\n".join(doc.page_content for doc in docs)

