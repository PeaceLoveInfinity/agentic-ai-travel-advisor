from llm.model_factory import get_model
from prompts.travel_prompts import BUDGET_PROMPT
from config.logger import logger

llm = get_model()


def generate_budget(
        destination,
        budget,
        duration
):

    logger.info(
        f"Budget calculation for {destination}"
    )

    prompt = f"""
    {BUDGET_PROMPT}

    Destination:
    {destination}

    Budget:
    {budget}

    Duration:
    {duration} days
    """

    response = llm.invoke(prompt)

    logger.info(
        "Budget generated"
    )

    return response.content