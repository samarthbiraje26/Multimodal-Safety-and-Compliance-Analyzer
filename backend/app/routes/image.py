from fastapi import APIRouter, UploadFile, File
from app.analyzers.image_analyzer import analyze_image

router = APIRouter(prefix="/api/image", tags=["Image"])

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    file_bytes = await file.read()
    return analyze_image(file_bytes)