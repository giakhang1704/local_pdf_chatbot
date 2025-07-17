from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate


template = """
Answer the question below.

Here is the conversation history: {context}
`
Question: {question}

Answer:
"""

llm = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | llm

def get_chain():
    print("✅ 1. Create model successfully.\n")
    return chain
    




