from pydantic import BaseModel


class RequirementRequest(BaseModel):
    requirement: str


class ChatRequest(BaseModel):
    question: str