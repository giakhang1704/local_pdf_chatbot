# Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
# .\chatbot\Scripts\Activate.ps1

from langchain_ollama import OllamaLLM
#from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import os

#os.environ["OPENAI_API_KEY"] = "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"

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
    




