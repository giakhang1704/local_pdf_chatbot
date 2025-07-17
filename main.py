from chatbot.model import get_chain
from loaders.pdf_loader import extract_text
from embedding.vector_store import save_vector_store, search_context
# import os

DB_DIR = "vectorDB"
CONVO_FILE = "conversation.txt"

def chat():
    chain = get_chain()
    memory = ""

    pdf_path = input("✅ 2. Enter path to your PDF file: ").strip()
    chunks = extract_text(pdf_path)
    save_vector_store(chunks)
    

    print("📚 PDF Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("❓ Question: ")
        if user_input.lower() == "exit":
            break

        context = search_context(user_input)
        full_context = memory + "\n" + context
        response = chain.invoke({"context": full_context.strip(), "question": user_input})
        print("\n💡 Answer:", response)
        print("\n")

        memory += f"\nUser: {user_input}\nAI: {response}\n"
        
        with open(CONVO_FILE, "a", encoding="utf-8") as f:
            f.write(f"User: {user_input}\nAI: {response}\n\n")
        
if __name__ == "__main__":
    chat()
