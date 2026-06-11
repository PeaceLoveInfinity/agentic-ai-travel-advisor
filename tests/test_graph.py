from graph.workflow import (
    travel_graph
)

state = {

    "destination": "Goa",

    "budget": 50000,

    "duration": 5
}

result = travel_graph.invoke(
    state
)

print(
    result["final_package"]
)