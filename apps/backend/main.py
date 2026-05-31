from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.services.ai_service import analyze_sprint_updates

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
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

    ai_response = analyze_sprint_updates(data.updates)

    return {
        "executive_summary": ai_response,
        "blockers": [],
        "risks": [],
        "action_items": []
    }

"""
#     updates = data.updates

#     blockers = []
#     risks = []
#     action_items = []

#     if "blocked" in updates.lower():
#         blockers.append("Team reported active blockers")

#     if "delay" in updates.lower():
#         risks.append("Potential sprint delivery delay")

#     if "qa" in updates.lower():
#         risks.append("QA dependency may impact release timeline")
    
#     if "approval" in updates.lower():
#         action_items.append("Follow up with leadership for approvals")
    
#     if "release" in updates.lower():
#         risks.append("Release coordination required")    

#     action_items.append("Review sprint priorities")
#     action_items.append("Schedule stakeholder sync")

#     summary = f"""
# Sprint analysis completed successfully.

# Key themes identified:
# - Delivery progress reported
# - Risk indicators detected
# - Stakeholder coordination required
# - Action items generated

# Original updates:
# {updates}
# """

#     return {
#     "executive_summary": summary,
#     "blockers": blockers,
#     "risks": risks,
#     "action_items": action_items
#     }
