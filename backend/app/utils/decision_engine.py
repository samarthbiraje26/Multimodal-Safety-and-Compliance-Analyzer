def decision_engine(label: str, confidence: float):
    if label != "safe" and confidence > 0.7:
        return "DANGER"
    elif label != "safe":
        return "WARNING"
    return "SAFE"