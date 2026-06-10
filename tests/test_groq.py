from llm.groq_client import get_llm

llm = get_llm()

response = llm.invoke(
    "Plan a 5-day trip to Goa"
)

print(response.content)