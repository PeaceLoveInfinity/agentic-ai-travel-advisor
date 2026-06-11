from graph.state import TravelState

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

from agents.supervisor_agent import (
    create_travel_package
)

def research_node(
        state: TravelState
):

    state["research_report"] = (
        research_destination(
            state["destination"]
        )
    )

    return state

def budget_node(
        state: TravelState
):

    state["budget_report"] = (
        generate_budget(
            state["destination"],
            state["budget"],
            state["duration"]
        )
    )

    return state

def hotel_node(
        state: TravelState
):

    state["hotel_report"] = (
        recommend_hotels(
            state["destination"],
            state["budget"]
        )
    )

    return state

def itinerary_node(
        state: TravelState
):

    state["itinerary_report"] = (
        generate_itinerary(
            state["destination"],
            state["duration"],
            state["budget"]
        )
    )

    return state

def risk_node(
        state: TravelState
):

    state["risk_report"] = (
        assess_risk(
            state["destination"]
        )
    )

    return state

def supervisor_node(
        state: TravelState
):

    state["final_package"] = (
        create_travel_package(
            state["destination"],
            state["duration"],
            state["budget"]
        )
    )

    return state