import httpx
import os
from dotenv import load_dotenv

load_dotenv()

class DevinClient:
    def __init__(self):
        self.api_key = os.getenv("DEVIN_API_KEY")
        self.org_id = os.getenv("DEVIN_ORG_ID")
        self.base_url = f"https://api.devin.ai/v3/organizations/{self.org_id}"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    async def create_session(self, prompt: str, repo_full_name: str = "tagaism/superset"):
        async with httpx.AsyncClient() as client:
            payload = {
                "prompt": prompt,
                "repos": [repo_full_name],
                "bypass_approval": True,
                "max_acu_limit": 50,
            }
            
            print(f"🔄 Creating Devin session for repo: {repo_full_name}")
            
            response = await client.post(
                f"{self.base_url}/sessions",
                json=payload,
                headers=self.headers
            )
            
            if response.status_code == 403:
                print("❌ 403 Forbidden - Permission issue")
                print("Response:", response.text)
            elif response.status_code != 200:
                print(f"❌ Error {response.status_code}")
                print("Response:", response.text)
            else:
                print("✅ Devin session created successfully!")
            
            response.raise_for_status()
            return response.json()