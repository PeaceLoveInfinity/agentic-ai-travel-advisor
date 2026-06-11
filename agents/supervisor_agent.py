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

from agents.itinerary_agent import (
    generate_itinerary
)

from agents.risk_agent import (
    assess_risk
)

from prompts.travel_prompts import (
    SUPERVISOR_PROMPT
)

from config.logger import logger


llm = get_model()


def create_travel_package(
        destination,
        duration,
        budget
):

    logger.info(
        f"Supervisor started for {destination}"
    )

    logger.info("Calling Research Agent")
    research_report = research_destination(
        destination
    )

    logger.info("Calling Budget Agent")
    budget_report = generate_budget(
        destination,
        budget,
        duration
    )

    logger.info("Calling Hotel Agent")
    hotel_report = recommend_hotels(
        destination,
        budget
    )

    logger.info("Calling Itinerary Agent")
    itinerary_report = generate_itinerary(
        destination,
        duration,
        budget
    )

    logger.info("Calling Risk Agent")
    risk_report = assess_risk(
        destination
    )

    prompt = f"""
    {SUPERVISOR_PROMPT}

    RESEARCH REPORT:
    {research_report}

    BUDGET REPORT:
    {budget_report}

    HOTEL REPORT:
    {hotel_report}

    ITINERARY REPORT:
    {itinerary_report}

    RISK REPORT:
    {risk_report}
    """

    response = llm.invoke(prompt)

    logger.info(
        "Travel package created"
    )

    return response.content