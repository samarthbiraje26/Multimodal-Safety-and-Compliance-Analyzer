from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    print("🔥 ROUTE HIT")
    print("Filename:", file.filename)

    return {
        "status": "SAFE",
        "debug": "route_working"
    }