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
        
        blocked_tickets = [
            ticket
            for ticket in jira_tickets
            if ticket["status"] == "Blocked"
        ]
        
        blocked_ticket_titles = [
        f'{ticket["key"]}: {ticket["title"]}'
        for ticket in blocked_tickets
        ]
        
        sprint_update = (
        data.updates
        if data.updates.strip()
            else "No sprint update provided."
        )

        combined_context = f"""
SPRINT UPDATE:
{sprint_update}

BLOCKED TICKETS:
{blocked_ticket_titles}

JIRA TICKETS:
{jira_tickets}

SLACK MESSAGES:
{slack_messages}
"""

        ai_result = analyze_sprint_updates(combined_context)

        ai_result["blockers"] = blocked_ticket_titles

        open_risks = [
            ticket
            for ticket in jira_tickets
            if ticket["status"] == "Blocked"
        ]

        ai_result["risks"] = [
            f'{ticket["key"]}: {ticket["title"]}'
            for ticket in open_risks
        ]

        release_approved = any(
            "approved" in message.lower()
            for message in slack_messages
        )

        testing_complete = any(
            "testing completed" in message.lower()
            or "testing complete" in message.lower()
            for message in slack_messages
        )

        has_blockers = len(blocked_ticket_titles) > 0
        has_risks = len(ai_result.get("risks", [])) > 0

        if has_blockers:
            ai_result["release_readiness"] = "At Risk"

        elif release_approved and testing_complete:
            ai_result["release_readiness"] = "Ready"

        else:
            ai_result["release_readiness"] = "Conditional"

        if ai_result["release_readiness"] == "Ready":
            ai_result["delivery_health_score"] = 95

        elif ai_result["release_readiness"] == "Conditional":
            ai_result["delivery_health_score"] = 85

        else:
            ai_result["delivery_health_score"] = 70

        return ai_result

    except Exception as e:
        return {
            "executive_summary": f"Backend error: {str(e)}",
            "blockers": [],
            "risks": [],
            "action_items": [],
            "delivery_health_score": 70,
            "release_readiness": "At Risk",
            "ai_confidence": 60,
            "executive_recommendation": "Review sprint risks and validate release readiness."
        }