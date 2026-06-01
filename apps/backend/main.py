from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.services.ai_service import analyze_sprint_updates
from src.services.jira_service import get_jira_tickets
from src.services.slack_service import get_slack_messages

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

@app.get("/delivery-context")
def delivery_context():
    return {
        "jira_tickets": get_jira_tickets(),
        "slack_messages": get_slack_messages()
        }

@app.post("/generate-summary")
def generate_summary(data: SprintInput):
    try:
        jira_tickets = get_jira_tickets()
        slack_messages = get_slack_messages()

        combined_context = f"""
SPRINT UPDATE:
{data.updates}

JIRA TICKETS:
{jira_tickets}

SLACK MESSAGES:
{slack_messages}
"""

        return analyze_sprint_updates(combined_context)

    except Exception as e:
        return {
            "executive_summary": f"Backend error: {str(e)}",
            "blockers": [],
            "risks": [],
            "action_items": []
        }