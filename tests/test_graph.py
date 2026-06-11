from graph.workflow import (
    travel_graph
)

state = {
    "destination": "Goa",
    "budget": 50000,
    "duration": 5
}

config = {
    "configurable": {
        "thread_id": "user_002"
    }
}

result = travel_graph.invoke(
    state,
    config=config
)

print(result)