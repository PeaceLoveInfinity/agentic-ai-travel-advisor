from agents.budget_agent import (
    generate_budget
)

report = generate_budget(
    destination="Goa",
    budget=50000,
    duration=5
)

print(report)