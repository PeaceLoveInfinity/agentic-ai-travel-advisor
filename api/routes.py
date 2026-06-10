from fastapi import APIRouter
from api.schemas import AskRequest
from api.schemas import ResearchRequest
from services.travel_ai import ask_travel_ai
from agents.research_agent import (research_destination)

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