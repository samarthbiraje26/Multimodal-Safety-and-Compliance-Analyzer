from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import text, image, audio, video

app = FastAPI(title="Multimodal Safety & Compliance Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(text.router, prefix="/api/text")
app.include_router(image.router, prefix="/api/image")
app.include_router(audio.router, prefix="/api/audio")
app.include_router(video.router, prefix="/api/video")

@app.get("/")
def root():
    return {"status": "Backend running"}