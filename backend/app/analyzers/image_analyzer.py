from PIL import Image
import io

async def analyze_image(file):
    # ✅ Read file correctly
    contents = await file.read()

    # ✅ Convert bytes → image
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    # 🔥 TEMP LOGIC (you can replace with ML later)
    # Example condition
    width, height = image.size

    if width > 500:
        return {"status": "DANGER"}
    else:
        return {"status": "SAFE"}