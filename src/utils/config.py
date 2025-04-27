import os
from dotenv import load_dotenv
from typing import Dict, Any

def load_config() -> Dict[str, Any]:
    """Load configuration from environment variables and .env file"""
    # Load environment variables from .env file
    load_dotenv()
    
    # Required configuration
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables")
    
    # Return configuration dictionary
    return {
        "GOOGLE_API_KEY": google_api_key,
        "EMBEDDING_MODEL": os.getenv("EMBEDDING_MODEL", "models/embedding-001"),
        "LLM_MODEL": os.getenv("LLM_MODEL", "gemini-2.0-flash"),
        "CHROMA_PERSIST_DIR": os.getenv("CHROMA_PERSIST_DIR", "./data/processed"),
        "CHUNK_SIZE": int(os.getenv("CHUNK_SIZE", "1000")),
        "CHUNK_OVERLAP": int(os.getenv("CHUNK_OVERLAP", "200"))
    }