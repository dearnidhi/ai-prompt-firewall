# app/api/routes.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.core.firewall import prompt_firewall

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    decision: str
    risk_score: float
    reason: str

@router.post("/check-prompt", response_model=PromptResponse)
def check_prompt(data: PromptRequest):
    result = prompt_firewall(data.prompt)
    return result
