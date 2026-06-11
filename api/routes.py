from fastapi import APIRouter
from services.travel_ai import ask_travel_ai
from api.schemas import AskRequest
from agents.research_agent import (research_destination)
from api.schemas import ResearchRequest
from agents.budget_agent import (generate_budget)
from api.schemas import BudgetRequest
from agents.hotel_agent import (recommend_hotels)
from api.schemas import HotelRequest
from agents.itinerary_agent import (generate_itinerary)
from api.schemas import (ItineraryRequest)
from agents.risk_agent import (assess_risk)
from api.schemas import (RiskRequest)
from agents.supervisor_agent import (create_travel_package)
from api.schemas import (TravelPackageRequest)
from graph.workflow import (travel_graph)

# Initializing the API router
router = APIRouter()

# Health check endpoint to verify that the API is running
@router.get("/")
def health():
    return {"status": "running"}

# This endpoint allows users to ask a question to the travel AI and get an answer
@router.post("/ask")
def ask_ai(payload: AskRequest):

    question = payload.question

    answer = ask_travel_ai(question)

    return {
        "answer": answer
    }

# This endpoint will perform research on a travel destination and return a report
@router.post("/research")

def research(payload: ResearchRequest):

    report = research_destination(
        payload.destination
    )

    return {
        "report": report
    }

# This endpoint will generate a budget report based on the destination, budget, and duration
@router.post("/budget")

def budget(payload: BudgetRequest):

    report = generate_budget(
        destination=payload.destination,
        budget=payload.budget,
        duration=payload.duration
    )

    return {
        "budget_report": report
    }

# This endpoint will recommend hotels based on the destination and budget
@router.post("/hotels")

def hotels(payload: HotelRequest):

    report = recommend_hotels(
        destination=payload.destination,
        budget=payload.budget
    )

    return {
        "hotel_report": report
    }

# This endpoint will generate an itinerary based on the destination, duration, and budget
@router.post("/itinerary")

def itinerary(
        payload: ItineraryRequest
):

    report = generate_itinerary(
        destination=payload.destination,
        duration=payload.duration,
        budget=payload.budget
    )

    return {
        "itinerary": report
    }

# This endpoint will assess the risk of traveling to a destination
@router.post("/risk")

def risk(
        payload: RiskRequest
):

    report = assess_risk(
        payload.destination
    )

    return {
        "risk_report": report
    }

# This endpoint will execute the entire supervisor agent workflow for creating a travel package
@router.post("/travel-package")

def travel_package(
        payload: TravelPackageRequest
):

    report = create_travel_package(
        destination=payload.destination,
        duration=payload.duration,
        budget=payload.budget
    )

    return {
        "travel_package": report
    }

# This endpoint will execute the entire graph workflow for creating a travel package
@router.post("/graph-travel")

def graph_travel(
        payload: TravelPackageRequest
):

    config = {
        "configurable": {
            "thread_id": "api_user_001"
        }
    }

    result = travel_graph.invoke(
        {
            "destination":
            payload.destination,

            "budget":
            payload.budget,

            "duration":
            payload.duration
        },
        config=config
    )

    return {
        "travel_package":
        result["final_package"]
    }