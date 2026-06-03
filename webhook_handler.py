from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/webhook")
@router.post("/")   # Catch both paths
async def github_webhook(request: Request):
    payload = await request.body()
    
    event = request.headers.get("X-GitHub-Event")
    try:
        data = await request.json()
    except:
        data = {}

    print(f"✅ Received {event} event | Action: {data.get('action')}")

    if event == "issues" and data.get("action") in ["opened", "labeled", "unlabeled"]:
        issue = data.get("issue", {})
        labels = [label["name"] for label in issue.get("labels", [])]
        
        if "devin-remediate" in labels:
            print(f"🚀 Triggering Devin for issue: {issue.get('title')}")
            from main import trigger_devin_session
            await trigger_devin_session(issue)
        else:
            print(f"Label 'devin-remediate' not found on issue: {issue.get('title')}")

    return {"status": "ok"}