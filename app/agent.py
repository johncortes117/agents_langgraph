from typing import TypedDict
from langgraph.graph import StateGraph, START, END


#Define the state of the agent
class State(TypedDict):
    customer_name: str
    message: str


#Define nodes
def node_1(state: State) -> State:
    state["message"] = "This is the message from node 1"
    return state

def node_2(state: State) -> State:
    customer_name = state["customer_name"]
    state["message"] = f"Hello {customer_name}, you are at node 2!"
    return state

def node_3(state: State) -> State:
    customer_name = state["customer_name"]
    state["message"] = f"Hi {customer_name}, you have just built your first agent with LangGraph!"
    return state


# Build the graph

builder = StateGraph(State)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)

builder.add_edge(START, "node_1")
builder.add_edge("node_1", "node_2")
builder.add_edge("node_2", "node_3")
builder.add_edge("node_3", END)

# Compile the graph
graph = builder.compile()