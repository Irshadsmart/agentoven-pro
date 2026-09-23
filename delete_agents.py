import os
import requests

BASE_URL = os.getenv("AGENTOVEN_URL")
SCOPED_KEY = os.getenv("AGENTOVEN_SCOPED_KEY")

agents_to_delete = [
    "hello-agent",
    "hello-agent-v2"
]

headers = {
    "Authorization": f"Bearer {SCOPED_KEY}",
    "Content-Type": "application/json"
}

for name in agents_to_delete:
    url = f"{BASE_URL}/api/v1/agents/{name}"
    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        print(f"Deleted agent: {name}")
    else:
        print(f"Failed to delete {name}: {response.status_code} - {response.text}")
