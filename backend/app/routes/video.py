from fastapi import APIRouter, UploadFile, File
from app.analyzers.video_analyzer import analyze_video
from app.utils.sms_alert import send_sms

router = APIRouter(prefix="/video", tags=["Video"])

@router.post("/analyze")
async def analyze_video_route(file: UploadFile = File(...)):
    result = analyze_video(file)

    if result["status"] == "DANGER":
        send_sms(f"🚨 VIDEO EMERGENCY DETECTED: {result['label']}")

    return result