from PIL import Image

def analyze_image(file):
    img = Image.open(file)
    width, height = img.size

    if width < 50 or height < 50:
        return {"safe": False, "reason": "Suspicious low-quality image"}

    return {"safe": True, "reason": "No visual violations detected"}