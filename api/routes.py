from fastapi import APIRouter
from api.schemas import AskRequest
from services.travel_ai import ask_travel_ai

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