from fastapi import APIRouter, UploadFile, File
from app.analyzers.video_analyzer import analyze_video

router = APIRouter(prefix="/video", tags=["Video"])

@router.post("/analyze")
async def analyze_video_route(file: UploadFile = File(...)):
    return analyze_video(file)