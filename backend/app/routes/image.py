from fastapi import APIRouter, UploadFile, File
from app.analyzers.image_analyzer import analyze_image
from app.utils.sms_alert import send_sms

router = APIRouter(prefix="/image", tags=["Image"])

@router.post("/analyze")
async def analyze_image_route(file: UploadFile = File(...)):
    result = analyze_image(file)

    if result["status"] == "DANGER":
        send_sms(f"🚨 IMAGE EMERGENCY DETECTED: {result['label']}")

    return result