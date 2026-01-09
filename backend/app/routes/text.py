from fastapi import APIRouter
from pydantic import BaseModel
from app.models.text_analyzer import analyze_text

router = APIRouter()

class TextInput(BaseModel):
    text: str

@router.post("/analyze")
def analyze(data: TextInput):
    return analyze_text(data.text)