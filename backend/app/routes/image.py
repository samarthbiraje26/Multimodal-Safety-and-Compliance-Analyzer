from fastapi import APIRouter, UploadFile, File
from app.analyzers.image_analyzer import analyze_image

router = APIRouter(prefix="/image", tags=["Image"])

@router.post("/analyze")
async def analyze_image_route(file: UploadFile = File(...)):
    return analyze_image(file)