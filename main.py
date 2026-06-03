from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Devin Superset Automation")

from webhook_handler import router
app.include_router(router)

@app.get("/")
async def health():
    return {"status": "✅ Devin Automation Service is running"}

async def trigger_devin_session(issue):
    from devin_client import DevinClient
    
    client = DevinClient()
    
    prompt = f"""You are an expert software engineer working on Apache Superset (fork: tagaism/superset).

Issue Title: {issue['title']}
Issue URL: {issue['html_url']}
Description: {issue.get('body') or 'No description provided.'}

Please fully address this issue:
1. Analyze the codebase thoroughly
2. Make the necessary code changes
3. Run relevant tests / linting if applicable
4. Create a clean Pull Request with good title and description
5. Link the PR back to this issue"""

    try:
        session = await client.create_session(prompt, "tagaism/superset")
        session_id = session.get('session_id')
        
        print(f"✅ Devin session created successfully! Session ID: {session_id}")
        
        if session_id:
            print(f"🔗 View session: https://app.devin.ai/organizations/{os.getenv('DEVIN_ORG_ID')}/sessions/{session_id}")
        
        return session_id
    except Exception as e:
        print(f"❌ Error creating Devin session: {e}")