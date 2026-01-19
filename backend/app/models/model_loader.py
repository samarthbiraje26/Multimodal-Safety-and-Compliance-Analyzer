import torch
from transformers import (
    pipeline,
    CLIPProcessor,
    CLIPModel,
    WhisperProcessor,
    WhisperForConditionalGeneration
)

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# TEXT – Toxicity
text_classifier = pipeline(
    "text-classification",
    model="unitary/toxic-bert",
    device=0 if DEVICE == "cuda" else -1
)

# IMAGE + VIDEO – CLIP
clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to(DEVICE)
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# AUDIO – Whisper
whisper_processor = WhisperProcessor.from_pretrained("openai/whisper-small")
whisper_model = WhisperForConditionalGeneration.from_pretrained(
    "openai/whisper-small"
).to(DEVICE)