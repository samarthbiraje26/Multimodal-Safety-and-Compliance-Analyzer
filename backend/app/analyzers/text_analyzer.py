from app.models.model_loader import text_classifier

def analyze_text(text: str):
    result = text_classifier(text)[0]

    score = float(result["score"])
    label = result["label"]

    if label != "LABEL_0" and score > 0.7:
        status = "DANGER"
    elif label != "LABEL_0":
        status = "WARNING"
    else:
        status = "SAFE"

    return {
        "status": status,
        "label": label,
        "confidence": round(score, 3)
    }