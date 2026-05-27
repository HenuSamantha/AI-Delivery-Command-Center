from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/test-summary")
def test_summary():
    return {
        "sprint": "Sprint 14",
        "summary": "Backend API scaffolding complete.",
        "blockers": [],
        "risks": ["No AI integration yet"],
        "action_items": ["Build AI summary engine next"]
    }