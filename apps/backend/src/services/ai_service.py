import json
from ollama import chat


def analyze_sprint_updates(updates: str) -> dict:
    prompt = f"""
You are an Engineering Delivery Analyst.

Analyze the sprint update below.

Return ONLY valid JSON.
Do not include markdown.
Do not include explanations outside the JSON.

Use this exact schema:

{{
  "executive_summary": "A concise summary",
  "blockers": ["Specific blocker"],
  "risks": ["Specific risk"],
  "action_items": ["Specific action item"],
  "delivery_health_score": 85,
  "release_readiness": "At Risk",
  "ai_confidence": 87,
  "executive_recommendation": "Specific leadership recommendation"
}}

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
            "action_items": [],
            "delivery_health_score": 70,
            "release_readiness": "At Risk",
            "ai_confidence": 60,
            "executive_recommendation": "Review sprint risks and validate release readiness."
        }