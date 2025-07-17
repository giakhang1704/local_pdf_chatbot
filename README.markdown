# PDF Chatbot

This project is a PDF Chatbot that allows users to interact with PDF documents by asking questions about their content. The chatbot processes both text-based and scanned (image-based) PDFs, extracts text, creates a vector store for semantic search, and uses a language model to generate answers based on the document's content and conversation history.

## Features
- Supports both text-based and scanned PDFs (via OCR).
- Extracts and chunks PDF content for efficient processing.
- Uses FAISS for vector-based similarity search to retrieve relevant document sections.
- Integrates with a language model (Llama3 via Ollama) for generating responses.
- Maintains conversation history for context-aware responses.
- Saves conversation logs to a file (`conversation.txt`).

## Project Structure
- `main.py`: Entry point for running the chatbot. Handles user input and orchestrates PDF processing, vector storage, and model inference.
- `model.py`: Defines the language model (Ollama with Llama3) and prompt template for generating responses.
- `vector_store.py`: Manages the FAISS vector store for embedding and searching document chunks.
- `pdf_loader.py`: Handles PDF loading, text extraction, and OCR for scanned PDFs.
- `vectorDB/`: Directory where the FAISS vector store is saved.
- `conversation.txt`: File where conversation history is logged.

## Prerequisites
- Python 3.8+
- A PDF file (text-based or scanned) to interact with.
- Optional: A local installation of Ollama with the Llama3 model for running the language model locally.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd pdf-chatbot
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv chatbot
   # On Windows
   .\chatbot\Scripts\Activate.ps1
   # On Unix/Linux/Mac
   source chatbot/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Tesseract OCR for scanned PDFs:
   - On Windows: Download and install from [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki).
   - On Ubuntu: `sudo apt-get install tesseract-ocr`
   - On macOS: `brew install tesseract`

5. Ensure Poppler is installed for PDF-to-image conversion:
   - On Windows: Download and add Poppler to your PATH from [Poppler](https://poppler.freedesktop.org/).
   - On Ubuntu: `sudo apt-get install poppler-utils`
   - On macOS: `brew install poppler`

6. (Optional) Install and configure Ollama:
   - Download and install Ollama from [Ollama](https://ollama.ai/).
   - Pull the Llama3 model: `ollama pull llama3`

## Usage
1. Run the chatbot:
   ```bash
   python main.py
   ```

2. Enter the path to your PDF file when prompted.
3. Ask questions about the PDF content. Type `exit` to quit.
4. Conversation history is saved to `conversation.txt`.

## Example
```bash
✅ 1. Create model successfully.

✅ 2. Enter path to your PDF file: sample.pdf

✅ 3. Detecting PDF type...

✅ 4. Text-based PDF. Load and split PDF file successfully.

✅ 5. Save vectorDB to local memory successfully.

📚 PDF Chatbot! Type 'exit' to quit.
❓ Question: What is the main topic of the PDF?
💡 Answer: The main topic of the PDF is...
```

## Dependencies
See `requirements.txt` for a complete list of Python dependencies.

## Notes
- The chatbot uses the `all-MiniLM-L6-v2` model from HuggingFace for embeddings. Ensure you have an internet connection for the initial download.
- Scanned PDFs require Tesseract and Poppler for OCR and image conversion.
- The vector store is saved locally in the `vectorDB/` directory and reused for subsequent queries.
- Conversation history is appended to `conversation.txt` for each session.

## License
This project is licensed under the MIT License.