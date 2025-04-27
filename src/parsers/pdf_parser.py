from PyPDF2 import PdfReader
from src.retrievers.vector_retriever import store_document_chunks

def process_pdf(file_path: str, domain: str):
    # Extract text from PDF
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    
    # Store in vector database
    store_document_chunks(text, domain)