from ollama import chat


def analyze_sprint_updates(updates: str) -> str:
    prompt = f"""
You are an Engineering Delivery Analyst.

Analyze the sprint update below and return a concise delivery intelligence report.

Use this exact format:

EXECUTIVE SUMMARY:
Write a concise leadership-ready summary.

RISKS:
- List delivery risks.

BLOCKERS:
- List blockers.

ACTION ITEMS:
- List recommended actions.

SPRINT UPDATE:
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

    return response["message"]["content"]