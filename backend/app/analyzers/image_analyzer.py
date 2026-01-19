from PIL import Image
import torch
from app.models.model_loader import clip_model, clip_processor, DEVICE

LABELS = [
    "safe content",
    "violent content",
    "weapon",
    "explicit content"
]

def analyze_image(file):
    image = Image.open(file).convert("RGB")

    inputs = clip_processor(
        text=LABELS,
        images=image,
        return_tensors="pt",
        padding=True
    ).to(DEVICE)

    with torch.no_grad():
        outputs = clip_model(**inputs)

    probs = outputs.logits_per_image.softmax(dim=1)[0]
    best = probs.argmax().item()

    return {
        "safe": LABELS[best] == "safe content",
        "label": LABELS[best],
        "confidence": round(probs[best].item(), 3)
    }