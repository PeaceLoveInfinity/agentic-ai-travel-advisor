from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

DATABASE_URL = os.getenv("DATABASE_URL")

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
