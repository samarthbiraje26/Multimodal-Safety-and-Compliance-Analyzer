from fastapi import APIRouter, UploadFile, File
from models.image_analyzer import analyze_image

router = APIRouter()

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    return analyze_image(file.file)