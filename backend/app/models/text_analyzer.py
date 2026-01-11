from app.models.model_loader import text_classifier

def analyze_text(text: str):
    result = text_classifier(text)[0]

    label = result["label"]
    score = float(result["score"])

    return {
        "safe": label == "LABEL_0",
        "label": label,
        "confidence": round(score, 3)
    }