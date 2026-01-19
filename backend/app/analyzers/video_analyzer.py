import cv2
import torch
from PIL import Image
from app.models.model_loader import clip_model, clip_processor, DEVICE

LABELS = [
    "safe content",
    "violent content",
    "weapon",
    "explicit content"
]

def analyze_video(path):
    cap = cv2.VideoCapture(path)
    frame_scores = []

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_id = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_id % fps == 0:  # 1 frame per second
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            inputs = clip_processor(
                text=LABELS,
                images=image,
                return_tensors="pt",
                padding=True
            ).to(DEVICE)

            with torch.no_grad():
                outputs = clip_model(**inputs)

            probs = outputs.logits_per_image.softmax(dim=1)[0]
            frame_scores.append(probs)

        frame_id += 1

    cap.release()

    avg_probs = torch.stack(frame_scores).mean(dim=0)
    best = avg_probs.argmax().item()

    return {
        "safe": LABELS[best] == "safe content",
        "label": LABELS[best],
        "confidence": round(avg_probs[best].item(), 3)
    }