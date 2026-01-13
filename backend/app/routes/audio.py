from fastapi import APIRouter, UploadFile, File
from app.analyzers.audio_analyzer import analyze_audio

router = APIRouter(prefix="/audio", tags=["Audio"])

@router.post("/analyze")
async def analyze_audio_route(file: UploadFile = File(...)):
    return analyze_audio(file)