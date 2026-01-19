# backend/app/models/model_loader.py

def text_classifier(text: str):
    if "help" in text.lower() or "danger" in text.lower():
        return {"status": "DANGER", "message": "Emergency text detected"}
    return {"status": "SAFE", "message": "No danger detected"}

def image_model(_):
    return {"status": "SAFE", "message": "Image looks safe"}

def audio_model(_):
    return {"status": "SAFE", "message": "Audio looks safe"}

def video_model(_):
    return {"status": "SAFE", "message": "Video looks safe"}