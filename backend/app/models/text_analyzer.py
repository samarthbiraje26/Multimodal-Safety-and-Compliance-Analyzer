def analyze_text(text: str):
    unsafe_keywords = ["violence", "hate", "kill", "weapon"]
    for word in unsafe_keywords:
        if word in text.lower():
            return {
                "safe": False,
                "reason": f"Detected unsafe keyword: {word}"
            }
    return {"safe": True, "reason": "Text is compliant"}