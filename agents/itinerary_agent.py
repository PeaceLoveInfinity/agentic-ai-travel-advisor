from llm.model_factory import get_model

from prompts.travel_prompts import (
    ITINERARY_PROMPT
)

from config.logger import logger


llm = get_model()


def generate_itinerary_from_state(
        state
):

    logger.info(
        f"Generating itinerary for {state['destination']}"
    )

    logger.info(
        "Using reports from LangGraph state"
    )

    prompt = f"""
    {ITINERARY_PROMPT}

    Destination:
    {state['destination']}

    Duration:
    {state['duration']}

    Research Report:
    {state['research_report']}

    Budget Report:
    {state['budget_report']}

    Hotel Report:
    {state['hotel_report']}
    """

    response = llm.invoke(
        prompt
    )

    logger.info(
        "Itinerary generated successfully"
    )

    return response.content