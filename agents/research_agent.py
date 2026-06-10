from llm.model_factory import get_model

from tools.tavily_tool import search_web

from prompts.travel_prompts import RESEARCH_PROMPT


llm = get_model()


def research_destination(destination):

    from config.logger import logger

    logger.info(f"Researching {destination}"
)

    search_results = search_web(
        f"Travel guide for {destination}"
    )

    prompt = f"""
    {RESEARCH_PROMPT}

    Destination:
    {destination}

    Search Results:
    {search_results}
    """

    response = llm.invoke(prompt)

    logger.info("Research completed")

    return response.content