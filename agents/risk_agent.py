from llm.model_factory import get_model

from tools.weather_tool import (
    get_weather
)

from prompts.travel_prompts import (
    RISK_PROMPT
)

from config.logger import logger


llm = get_model()


def assess_risk(destination):

    logger.info(
        f"Assessing risks for {destination}"
    )

    weather_data = get_weather(
        destination
    )

    prompt = f"""
    {RISK_PROMPT}

    Destination:
    {destination}

    Weather Data:
    {weather_data}
    """

    response = llm.invoke(prompt)

    logger.info(
        "Risk assessment completed"
    )

    return response.content