import json
from ollama import chat


def analyze_sprint_updates(updates: str) -> dict:
    prompt = f"""
You are an Engineering Delivery Analyst responsible for assessing delivery health, release readiness, and operational risk.

You must evaluate:

- Jira ticket status
- Slack delivery signals
- Sprint updates

Use evidence from all sources before making recommendations.

Do not exaggerate risks.
Do not assume blockers exist unless they are explicitly present.

When determining release readiness:

Ready:
- No blockers
- Release approved
- Testing completed

Conditional:
- Minor risks remain
- Testing still in progress

At Risk:
- Blockers exist
- Critical testing issues remain

Always justify your release readiness decision using the provided data.

Return ONLY valid JSON.
Do not include markdown.
Do not include explanations outside the JSON.

Use this exact schema:

{{
  "executive_summary": "A concise summary",
  "blockers": ["Specific blocker"],
  "risks": ["Specific risk"],
  "risk_severity": "Low",
  "action_items": ["Specific action item"],
  "delivery_health_score": 85,
  "release_readiness": "At Risk",
  "ai_confidence": 87,
  "executive_recommendation": "Specific leadership recommendation"
}}

Risk Severity Rules:

Low:
- 0 blockers
- 0-1 risks

Medium:
- 1 blocker
- 2-3 risks

High:
- Multiple blockers
- Release at risk

Populate all fields with actual analysis.

Do NOT use placeholder values such as:
"string"
"example"
"sample"

Generate real blockers, risks, action items, delivery health score, release readiness, AI confidence, and executive recommendation.

Release Readiness Rules:

Ready:
- No blockers exist
- Release approval has been received
- Testing is complete

Conditional:
- Minor risks remain
- Testing is still in progress
- Non-critical dependencies remain

At Risk:
- One or more blockers exist
- Release approval is still pending
- Critical testing issues remain
- Major delivery risks are present

Determine release_readiness using these rules.
Important source-of-truth rules:

- Jira ticket status is the source of truth for blockers.
- Only tickets with status "Blocked" may be listed as blockers.
- Tickets with status "Done" are not blockers or risks.
- Tickets with status "In QA" are not blockers.
- Do not create blockers that are not present in the BLOCKED TICKETS section.
- Risks may come from Slack signals, sprint updates, or non-blocking Jira concerns, but completed tickets should not be classified as risks.

If no sprint update is provided, do not invent risks, blockers, or dependencies.
Base your analysis only on Jira tickets and Slack messages.

If there are no blocked tickets, release approval has been received, and testing is complete, release_readiness should be "Ready" unless critical risks are explicitly stated.

Do not infer blockers.
Do not infer release approval issues.
Do not infer testing issues.
Use only evidence provided in the sprint update, Jira tickets, and Slack messages.

If no sprint update is provided, do not create a risk based on the absence of a sprint update.

Sprint Update:

{updates}
"""

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    content = response["message"]["content"]

    content = content.replace("```json", "")
    content = content.replace("```", "")
    content = content.strip()

    start = content.find("{")
    end = content.rfind("}") + 1

    if start != -1 and end != 0:
        content = content[start:end]

    if content.count("{") > content.count("}"):
        content += "}"
    
    try:
        return json.loads(content)

    except Exception as e:
        print("RAW AI RESPONSE:")
        print(content)
        print(f"Error parsing JSON: {e}")

        return {
            "executive_summary": content,
            "blockers": [],
            "risks": [],
            "risk_severity": "Medium",
            "action_items": [],
            "delivery_health_score": 70,
            "release_readiness": "At Risk",
            "ai_confidence": 60,
            "executive_recommendation": "Review sprint risks and validate release readiness."
        }