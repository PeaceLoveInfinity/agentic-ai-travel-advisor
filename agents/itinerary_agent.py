from llm.model_factory import get_model

from agents.research_agent import (
    research_destination
)

from agents.budget_agent import (
    generate_budget
)

from agents.hotel_agent import (
    recommend_hotels
)

from prompts.travel_prompts import (
    ITINERARY_PROMPT
)

from config.logger import logger


llm = get_model()


def generate_itinerary(
        destination,
        duration,
        budget
):

    logger.info(
        f"Creating itinerary for {destination}"
    )

    logger.info(
        "Calling Research Agent"
    )

    research_report = research_destination(
        destination
    )

    logger.info(
        "Calling Budget Agent"
    )

    budget_report = generate_budget(
        destination,
        budget,
        duration
    )

    logger.info(
        "Calling Hotel Agent"
    )

    hotel_report = recommend_hotels(
        destination,
        budget
    )

    prompt = f"""
    {ITINERARY_PROMPT}

    Destination:
    {destination}

    Duration:
    {duration}

    Research Report:
    {research_report}

    Budget Report:
    {budget_report}

    Hotel Report:
    {hotel_report}
    """

    response = llm.invoke(prompt)

    logger.info(
        "Itinerary created"
    )

    return response.content