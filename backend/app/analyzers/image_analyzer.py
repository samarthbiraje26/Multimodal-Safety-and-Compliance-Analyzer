from PIL import Image
from io import BytesIO

def analyze_image(file_bytes: bytes):
    image = Image.open(BytesIO(file_bytes)).convert("RGB")

    # 🔴 TEMP LOGIC (Replace with ML later)
    width, height = image.size

    if width > 500:
        return {
            "status": "DANGER",
            "message": "Danger detected in image"
        }

    return {
        "status": "SAFE",
        "message": "No danger detected"
    }