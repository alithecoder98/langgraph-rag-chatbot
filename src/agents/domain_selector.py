from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from src.utils.config import load_config

config = load_config()

class DomainSelector:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            google_api_key=config["GOOGLE_API_KEY"],
            temperature=0.1
        )
        
        self.prompt = ChatPromptTemplate.from_template(
            """Based on the user's input and selected domain '{domain}', 
            determine if we need to request additional domain-specific information.
            Return 'yes' if we need more domain context, otherwise 'no'.
            
            User input: {input}
            
            Decision:"""
        )
        
        self.chain = self.prompt | self.llm | StrOutputParser()
    
    def process(self, state):
        # In our current flow, we already have the domain from user selection
        # So we'll just pass it through
        # In a more complex version, this could validate or refine the domain
        return state