from llm.model_factory import get_model
from config.logger import logger

llm = get_model()

def ask_travel_ai(query):

    logger.info(f"Question: {query}")

    response = llm.invoke(query)

    logger.info("Response generated")

    return response.content