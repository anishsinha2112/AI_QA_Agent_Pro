from pydantic import BaseModel


class RequirementRequest(BaseModel):
    requirement: str