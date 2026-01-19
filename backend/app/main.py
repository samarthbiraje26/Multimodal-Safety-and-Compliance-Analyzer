from fastapi import FastAPI
from app.routes import text, image, audio, video

app = FastAPI()

app.include_router(text.router)
app.include_router(image.router)
app.include_router(audio.router)
app.include_router(video.router)