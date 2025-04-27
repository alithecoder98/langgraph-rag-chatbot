import os
import tempfile
import streamlit as st
from src.graph.main_graph import get_agent_executor
from src.utils.config import load_config
from src.parsers.pdf_parser import process_pdf
from src.parsers.web_parser import process_url

# Load configuration
config = load_config()

def main():
    st.title("Document Understanding Assistant")
    
    # Initialize session state
    if "documents_processed" not in st.session_state:
        st.session_state.documents_processed = False
    if "agent" not in st.session_state:
        st.session_state.agent = get_agent_executor()
    
    # Domain selection
    domain = st.selectbox(
        "Select your document domain",
        ["Engineering", "Medical", "Legal", "Communication", "Other"]
    )
    
    # Document input options
    input_option = st.radio(
        "How would you like to provide documents?",
        ["Upload PDF", "Enter URL"]
    )
    
    if input_option == "Upload PDF":
        uploaded_files = st.file_uploader(
            "Upload PDF documents", 
            type=["pdf"],
            accept_multiple_files=True
        )
        
        if uploaded_files and st.button("Process Documents"):
            with st.spinner("Processing documents..."):
                for file in uploaded_files:
                    with tempfile.NamedTemporaryFile(delete=False) as tmp:
                        tmp.write(file.getvalue())
                        process_pdf(tmp.name, domain)
                st.session_state.documents_processed = True
                st.success("Documents processed successfully!")
    
    elif input_option == "Enter URL":
        url = st.text_input("Enter document URL")
        if url and st.button("Process URL"):
            with st.spinner("Processing URL..."):
                process_url(url, domain)
                st.session_state.documents_processed = True
                st.success("URL content processed successfully!")
    
    # Chat interface
    if st.session_state.documents_processed:
        st.subheader("Ask about your documents")
        user_query = st.text_input("Your question")
        
        if user_query:
            with st.spinner("Generating answer..."):
                response = st.session_state.agent.invoke({
                    "input": user_query,
                    "domain": domain
                })
                st.write(response["output"])

if __name__ == "__main__":
    main()