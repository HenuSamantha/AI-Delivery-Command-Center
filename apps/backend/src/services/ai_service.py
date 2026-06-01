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
  "action_items": ["Specific action item"]
}}

Populate all fields with actual analysis.

Do NOT use placeholder values such as:
"string"
"example"
"sample"

Generate real blockers, risks, and action items.

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

    if start != -1 and end != -1:
        content = content[start:end]

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
            "action_items": []
        }