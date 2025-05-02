from typing import TypedDict

#Define the state of the agent
class State(TypedDict):
    my_var: str
    customer_name: str

#Define nodes
def node_1(state: State) -> State:
    state["my_var"] = "Hello"
    state["customer_name"] = "John"
    return state

def node_2(state: State) -> State:
    customer_name = state["customer_name"]
    state["my_var"] = f"Hello {customer_name}"
    return state

def node_3(state: State) -> State:
    return state