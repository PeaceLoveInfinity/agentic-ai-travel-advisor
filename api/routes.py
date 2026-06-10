from fastapi import APIRouter
from services.travel_ai import ask_travel_ai
from api.schemas import AskRequest
from agents.research_agent import (research_destination)
from api.schemas import ResearchRequest
from agents.budget_agent import (generate_budget)
from api.schemas import BudgetRequest

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