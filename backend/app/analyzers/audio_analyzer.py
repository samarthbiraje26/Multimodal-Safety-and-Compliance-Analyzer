from ..models.model_loader import audio_model
from backend.app.models.model_loader import (
    whisper_model,
    whisper_processor,
    DEVICE
)
from app.analyzers.text_analyzer import analyze_text

def analyze_audio(path):
    waveform, sample_rate = torchaudio.load(path)

    inputs = whisper_processor(
        waveform.squeeze(),
        sampling_rate=sample_rate,
        return_tensors="pt"
    ).to(DEVICE)

    with torch.no_grad():
        predicted_ids = whisper_model.generate(inputs.input_features)

    transcription = whisper_processor.batch_decode(
        predicted_ids,
        skip_special_tokens=True
    )[0]

    text_result = analyze_text(transcription)

    return {
        "transcription": transcription,
        "analysis": text_result
    }