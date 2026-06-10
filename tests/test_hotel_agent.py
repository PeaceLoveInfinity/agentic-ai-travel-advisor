from agents.hotel_agent import (
    recommend_hotels
)

report = recommend_hotels(
    destination="Goa",
    budget=50000
)

print(report)