try:
    from langchain_chroma import Chroma
    USING_OFFICIAL_CHROMA = True
except ImportError:
    try:
        from langchain_community.vectorstores import Chroma
        USING_OFFICIAL_CHROMA = False
        import warnings
        warnings.warn("Using community Chroma - install langchain-chroma for better support")
    except ImportError as e:
        raise ImportError(
            "Could not import Chroma. Please install either:\n"
            "1. Official package: pip install langchain-chroma\n"
            "2. Community package: pip install langchain-community"
        ) from e

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.utils.config import load_config

config = load_config()

# Initialize components
embeddings = GoogleGenerativeAIEmbeddings(
    model=config["EMBEDDING_MODEL"],
    google_api_key=config["GOOGLE_API_KEY"]
)

vector_store = Chroma(
    persist_directory=config["CHROMA_PERSIST_DIR"],
    embedding_function=embeddings
)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=config["CHUNK_SIZE"],
    chunk_overlap=config["CHUNK_OVERLAP"]
)

def store_document_chunks(text: str, domain: str):
    """Process and store document chunks with domain metadata"""
    chunks = text_splitter.split_text(text)
    metadatas = [{"domain": domain} for _ in chunks]
    vector_store.add_texts(chunks, metadatas=metadatas)