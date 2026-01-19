from fastapi import APIRouter, UploadFile, File
from app.analyzers.image_analyzer import analyze_image

router = APIRouter()

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    result = await analyze_image(file)
    return result