from langchain_groq import ChatGroq
from config.settings import GROQ_API_KEY


def get_llm():

    llm = ChatGroq(
        api_key=GROQ_API_KEY,
        model="llama-3.1-8b-instant",
        temperature=0.3
    )

    return llm