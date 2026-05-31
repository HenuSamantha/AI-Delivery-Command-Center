from src.services.ai_service import analyze_sprint_updates

result = analyze_sprint_updates(
    """
    QA environment is blocked.
    Release approval is pending.
    Backend integration completed.
    """
)

print(result)