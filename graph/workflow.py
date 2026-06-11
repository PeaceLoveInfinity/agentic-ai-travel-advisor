# This file defines the workflow for the Travel Advisor application using a state graph.
from langgraph.graph import (
    StateGraph,
    END
)

# Importing the TravelState which will be used as the state for the graph
from graph.state import TravelState

# Importing node functions that will be used in the graph
from graph.nodes import (
    research_node,
    budget_node,
    hotel_node,
    itinerary_node,
    risk_node,
    supervisor_node
)
# Importing the checkpoint manager to handle memory checkpoints in the workflow
from memory.checkpoint_manager import (checkpointer)

# Creating the graph builder instance

builder = StateGraph(
    TravelState
)

# Building Nodes for the graph, each node corresponds to an agent's task

builder.add_node(
    "research",
    research_node
)

builder.add_node(
    "budget",
    budget_node
)

builder.add_node(
    "hotel",
    hotel_node
)

builder.add_node(
    "itinerary",
    itinerary_node
)

builder.add_node(
    "risk",
    risk_node
)

builder.add_node(
    "supervisor",
    supervisor_node
)

# Adding Edges to define the flow of the graph

builder.set_entry_point(
    "research"
)

builder.add_edge(
    "research",
    "budget"
)

builder.add_edge(
    "budget",
    "hotel"
)

builder.add_edge(
    "hotel",
    "itinerary"
)

builder.add_edge(
    "itinerary",
    "risk"
)

builder.add_edge(
    "risk",
    "supervisor"
)

builder.add_edge(
    "supervisor",
    END
)

# Compiling the graph with the checkpointer to enable memory management and checkpointing during the workflow execution
travel_graph = builder.compile(checkpointer=checkpointer)