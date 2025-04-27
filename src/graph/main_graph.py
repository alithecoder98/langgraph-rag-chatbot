from typing import TypedDict, Annotated, Sequence
import operator
from langgraph.graph import StateGraph, END
from src.agents.query_agent import QueryAgent

class AgentState(TypedDict):
    input: str
    domain: str
    documents: Annotated[Sequence[str], operator.add]
    output: str

def get_agent_executor():
    # Initialize agents
    query_agent = QueryAgent()
    
    # Define workflow
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("query_agent", query_agent.process)
    
    # Set entry point directly to query agent for now
    workflow.set_entry_point("query_agent")
    
    # End after query
    workflow.add_edge("query_agent", END)
    
    # Compile the graph
    return workflow.compile()