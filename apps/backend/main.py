from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.services.ai_service import analyze_sprint_updates

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SprintInput(BaseModel):
    updates: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate-summary")
def generate_summary(data: SprintInput):
    try:
        return analyze_sprint_updates(data.updates)
    except Exception as e:
        return {
            "executive_summary": f"Backend error: {str(e)}",
            "blockers": [],
            "risks": [],
            "action_items": []
        }