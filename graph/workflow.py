from langgraph.graph import (StateGraph, END)
from graph.state import TravelState
from graph.nodes import (
    research_node,
    budget_node,
    hotel_node,
    itinerary_node,
    risk_node,
    supervisor_node
)
from memory.checkpoint_manager import (checkpointer)
from graph.nodes import (approval_node)

# Creating the graph builder instance
builder = StateGraph(TravelState)

# Building Nodes for the graph, each node corresponds to an agent's task
builder.add_node("research", research_node)

builder.add_node("budget", budget_node)

builder.add_node("hotel", hotel_node)

builder.add_node("itinerary", itinerary_node)

builder.add_node("risk", risk_node)

builder.add_node("supervisor", supervisor_node)

builder.add_node("approval", approval_node)

# Adding Edges to define the flow of the graph
builder.set_entry_point("research")

builder.add_edge("research", "budget")

builder.add_edge("budget", "hotel")

builder.add_edge("hotel", "itinerary")

builder.add_edge("itinerary", "risk")

builder.add_edge("risk", "supervisor")

builder.add_edge("supervisor", "approval")

def approval_router(
        state
):

    if (
        state["approval_status"]
        == "yes"
    ):
        return "approved"

    return "rejected"

builder.add_conditional_edges(
    "approval",
    approval_router,
    {
        "approved": END,

        "rejected":
        "supervisor"
    }
)

# Compiling the graph with the checkpointer to enable memory management and checkpointing during the workflow execution
travel_graph = builder.compile(checkpointer=checkpointer)