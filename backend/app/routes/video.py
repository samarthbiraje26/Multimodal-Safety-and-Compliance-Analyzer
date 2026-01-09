from fastapi import APIRouter, UploadFile, File
import shutil
from app.models.video_analyzer import analyze_video

router = APIRouter()

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    path = f"temp_{file.filename}"
    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return analyze_video(path)