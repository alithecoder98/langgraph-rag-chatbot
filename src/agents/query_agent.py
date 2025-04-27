from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from src.retrievers.vector_retriever import vector_store
from src.utils.config import load_config

config = load_config()

class QueryAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",  # Updated to latest model
            google_api_key=config["GOOGLE_API_KEY"],
            temperature=0.3
        )
        
        self.retriever = vector_store.as_retriever(
            search_kwargs={"k": 3, "filter": {"domain": ""}}
        )
        
        self.prompt = ChatPromptTemplate.from_template(
            """You are an expert assistant specialized in {domain} documents.
            Use the following context to answer the question at the end.
            
            Context: {context}
            
            Question: {question}
            
            Provide a detailed answer:"""
        )
        
        self.chain = (
            {
                "context": lambda x: self.retriever.invoke(x["input"]),  # Updated method
                "question": lambda x: x["input"],
                "domain": lambda x: x["domain"]
            }
            | self.prompt
            | self.llm
            | StrOutputParser()
        )
    
    def process(self, state):
        state["output"] = self.chain.invoke(state)
        return state