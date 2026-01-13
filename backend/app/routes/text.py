from fastapi import APIRouter
from app.analyzers.text_analyzer import analyze_text

router = APIRouter(prefix="/text", tags=["Text"])

@router.post("/analyze")
def analyze_text_route(data: dict):
    return analyze_text(data["text"])