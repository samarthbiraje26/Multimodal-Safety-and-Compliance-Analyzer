from fastapi import APIRouter, UploadFile, File
from app.analyzers.image_analyzer import analyze_image

router = APIRouter(
    prefix="/api/image",
    tags=["Image Analysis"]
)

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    return await analyze_image(file)