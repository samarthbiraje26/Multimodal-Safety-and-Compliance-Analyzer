from fastapi import APIRouter, UploadFile, File
from app.analyzers.audio_analyzer import analyze_audio
from app.utils.sms_alert import send_sms

router = APIRouter(prefix="/audio", tags=["Audio"])

@router.post("/analyze")
async def analyze_audio_route(file: UploadFile = File(...)):
    result = analyze_audio(file)

    if result["status"] == "DANGER":
        send_sms(f"🚨 AUDIO EMERGENCY DETECTED: {result['label']}")

    return result