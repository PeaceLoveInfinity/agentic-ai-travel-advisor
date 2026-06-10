from agents.itinerary_agent import (
    generate_itinerary
)

result = generate_itinerary(
    destination="Goa",
    duration=5,
    budget=50000
)

print(result)