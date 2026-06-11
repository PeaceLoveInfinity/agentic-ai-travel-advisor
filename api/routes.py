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

router = APIRouter()

@router.get("/")
def health():
    return {"status": "running"}


@router.post("/ask")
def ask_ai(payload: AskRequest):

    question = payload.question

    answer = ask_travel_ai(question)

    return {
        "answer": answer
    }


@router.post("/research")

def research(payload: ResearchRequest):

    report = research_destination(
        payload.destination
    )

    return {
        "report": report
    }


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


@router.post("/hotels")

def hotels(payload: HotelRequest):

    report = recommend_hotels(
        destination=payload.destination,
        budget=payload.budget
    )

    return {
        "hotel_report": report
    }


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