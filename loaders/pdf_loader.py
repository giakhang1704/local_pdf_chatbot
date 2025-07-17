from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import pdfplumber
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
from langchain.schema import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def extract_text(file_path):
    print("\n✅ 3. Detecting PDF type...\n")
    if is_scanned_pdf(file_path):
        return pdf_ocr(file_path)
    else:
        return pdf_text(file_path)
    

def is_scanned_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text and text.strip():
                    return False
    except Exception as e:
        print(f"⚠️ Error while checking PDF type: {e}")
    return True


def pdf_ocr(pdf_path: str):
    images = convert_from_path(pdf_path)
    documents = []

    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image)
        documents.append(Document(page_content=text, metadata={"page": i + 1}))

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)
    print("✅ 4. Image-based PDF. Load and OCR-extract PDF content successfully.\n")
    return chunks


def pdf_text(pdf_path: str):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    
    chunks = splitter.split_documents(documents)
    print("✅ 4. Text-based PDF. Load and split PDF file successfully.\n")
    return chunks
