from agents.supervisor_agent import (
    create_travel_package
)

report = create_travel_package(
    destination="Goa",
    duration=5,
    budget=50000
)

print(report)