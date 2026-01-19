from PIL import Image
from io import BytesIO

async def analyze_image(file):
    contents = await file.read()        # ✅ await coroutine
    image = Image.open(BytesIO(contents)).convert("RGB")

    # TODO: run your ML model here
    return {
        "status": "success",
        "message": "Image analyzed successfully"
    }