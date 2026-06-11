from llm.model_factory import (
    get_model
)

from prompts.travel_prompts import (
    SUPERVISOR_PROMPT
)

llm = get_model()


def build_package(
        state
):

    prompt = f"""
    {SUPERVISOR_PROMPT}

    RESEARCH REPORT:
    {state['research_report']}

    BUDGET REPORT:
    {state['budget_report']}

    HOTEL REPORT:
    {state['hotel_report']}

    ITINERARY REPORT:
    {state['itinerary_report']}

    RISK REPORT:
    {state['risk_report']}
    """

    response = llm.invoke(
        prompt
    )

    return response.content