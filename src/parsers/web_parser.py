import requests
from bs4 import BeautifulSoup
from src.retrievers.vector_retriever import store_document_chunks

def process_url(url: str, domain: str):
    # Fetch and parse web content
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract main content (simplified - would need customization)
    text = ' '.join([p.get_text() for p in soup.find_all('p')])
    
    # Store in vector database
    store_document_chunks(text, domain)