# Document Understanding Assistant with LangGraph

A powerful RAG (Retrieval-Augmented Generation) chatbot that helps users understand complex documents by allowing PDF uploads or URL processing, with domain-specific customization.

## Features

- 📄 **Multi-source ingestion**: Process both PDF uploads and webpage URLs
- 🏷️ **Domain-aware processing**: Specialized handling for engineering, medical, legal, and other domains
- 🔍 **Semantic search**: Vector-based retrieval for accurate context finding
- 💬 **Conversational interface**: Natural language question answering about documents
- ⚡ **Real-time processing**: Immediate availability after upload
- 🧠 **Google Gemini integration**: Leverages cutting-edge LLM capabilities

## Tech Stack

- **Framework**: LangGraph (for agent orchestration)
- **LLM**: Google Gemini 1.5 Flash/Pro
- **Vector Store**: ChromaDB
- **Frontend**: Streamlit
- **Document Processing**: PyPDF, BeautifulSoup
- **Environment**: Python 3.10+

## Getting Started

### Prerequisites

- Python 3.10 or later
- Google Cloud API key with Generative AI access
- [Poetry](https://python-poetry.org/) (recommended) or pip

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/document-understanding-assistant.git
cd document-understanding-assistant

# Install dependencies (using pip)
pip install -r requirements.txt

# Alternative using poetry
poetry install

Configuration

    Create a .env file in the project root:

env

GOOGLE_API_KEY=your_api_key_here

    (Optional) Configure additional settings in src/utils/config.py

Usage
bash

# Run the Streamlit application
streamlit run app.py

The application will launch in your default browser at http://localhost:8501
Project Structure

document-understanding-assistant/
├── data/                   # Processed document storage
├── src/
│   ├── agents/             # LangGraph agents
│   ├── chains/             # LangChain components
│   ├── graph/              # LangGraph workflows
│   ├── parsers/            # Document parsers
│   ├── retrievers/         # Vector store operations
│   └── utils/              # Configuration and helpers
├── tests/                  # Unit tests
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
└── README.md               # This file

Customization
Adding New Domains

    Edit app.py to add new domain options

    Create domain-specific prompts in src/agents/query_agent.py

    Update the domain classifier in src/agents/domain_selector.py

Supported File Types
Format	Support Level	Notes
PDF	                          ✅ Full	Text extraction
Web URLs	                    ✅ Full	Content scraping
DOCX	                        ⚠️ Partial	Requires unstructured
PPTX	                        ⚠️ Partial	Requires unstructured

Contributing

We welcome contributions! Please follow these steps:

    Fork the repository

    Create a feature branch (git checkout -b feature/your-feature)

    Commit your changes (git commit -m 'Add some feature')

    Push to the branch (git push origin feature/your-feature)

    Open a Pull Request

    LangChain/LangGraph team for the amazing orchestration framework

    Google DeepMind for the Gemini models

    Chroma team for the lightweight vector store
