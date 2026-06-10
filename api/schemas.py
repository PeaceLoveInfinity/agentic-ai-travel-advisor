from pydantic import BaseModel


class AskRequest(BaseModel):
    question: str

class ResearchRequest(BaseModel):
    destination: str

class BudgetRequest(BaseModel):

    destination: str

    budget: int

    duration: int