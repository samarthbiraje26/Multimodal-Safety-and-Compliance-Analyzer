🛡️ Multimodal Safety & Compliance Analyzer

An end-to-end AI-powered Multimodal Safety & Compliance Analyzer that evaluates Text, Images, Audio, and Video content for potential policy violations using state-of-the-art machine learning models.
This project demonstrates real-world AI system design, modular architecture, and full-stack integration.

🚀 Features
✅ Text Safety Analysis (toxicity, harmful language)
✅ Image Safety Analysis (violence, weapons, explicit content)
✅ Audio Safety Analysis (speech-to-text + toxicity detection)
✅ Video Safety Analysis (frame sampling + visual safety)
✅ Confidence scores for predictions
✅ Modern React frontend
✅ FastAPI backend
✅ Production-style ML integration
✅ CPU-friendly (GPU optional)

🧠 AI / ML Models Used
Text : unitary/toxic-bert (DistilBERT)	Toxicity & harmful language detection
Image :	openai/clip-vit-base-patch32	Zero-shot visual safety classification
Audio	: openai/whisper-small	Speech-to-text
Video :	CLIP + frame sampling	Unsafe visual content detection

Design Principle:
Instead of one heavy multimodal model, the system uses specialized models per modality, which is how real-world AI systems are built.

🏗️ System Architecture
Frontend (React)
   |
   | REST API
   v
Backend (FastAPI)
   |
   |── Text Analyzer   → DistilBERT
   |── Image Analyzer  → CLIP
   |── Audio Analyzer  → Whisper → DistilBERT
   |── Video Analyzer  → Frame Sampling → CLIP

⚙️ Setup & Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/multimodal-safety-analyzer.git
cd multimodal-safety-analyzer

🔧 Backend Setup (FastAPI + ML)
Install Dependencies
cd backend
pip install -r requirements.txt

Run Backend Server
uvicorn app.main:app --reload

Backend will run at:
http://localhost:8000

Test:
http://localhost:8000/

🎨 Frontend Setup (React)

Install Dependencies
cd frontend
npm install

Run Frontend
npm run dev

Frontend will run at:
http://localhost:5173
