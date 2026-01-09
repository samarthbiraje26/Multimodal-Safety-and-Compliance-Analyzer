from fastapi import APIRouter, UploadFile, File
from models.audio_analyzer import analyze_audio

router = APIRouter()

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    return analyze_audio(file.filename)