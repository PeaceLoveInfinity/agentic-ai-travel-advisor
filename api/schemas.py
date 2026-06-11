from pydantic import BaseModel


class AskRequest(BaseModel):
    question: str

class ResearchRequest(BaseModel):
    destination: str

class BudgetRequest(BaseModel):

    destination: str

    budget: int

    duration: int

class HotelRequest(BaseModel):

    destination: str

    budget: int

class ItineraryRequest(BaseModel):

    destination: str

    duration: int

    budget: int

class RiskRequest(BaseModel):

    destination: str

class TravelPackageRequest(
    BaseModel
):

    destination: str

    duration: int

    budget: int

class ApprovalRequest(
    BaseModel
):

    thread_id: str

    decision: str