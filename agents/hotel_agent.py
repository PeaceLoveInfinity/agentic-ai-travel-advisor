from llm.model_factory import get_model

from tools.location_tool import (
    search_location
)

from prompts.travel_prompts import HOTEL_PROMPT

from config.logger import logger


llm = get_model()


def recommend_hotels(
        destination,
        budget
):

    logger.info(
        f"Finding hotels for {destination}"
    )

    hotel_data = search_location(
        f"Hotels in {destination}"
    )

    prompt = f"""
    {HOTEL_PROMPT}

    Destination:
    {destination}

    Budget:
    {budget}

    Hotel Data:
    {hotel_data}
    """

    response = llm.invoke(prompt)

    logger.info(
        "Hotel recommendation completed"
    )

    return response.content