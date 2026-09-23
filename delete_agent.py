"""
Delete Agent - Clean up old agent so we can recreate it
"""
from agentoven.client import AgentOvenClient
import os
import config

client = AgentOvenClient(
    url=os.getenv("AGENTOVEN_URL"),
    api_key=os.getenv("AGENTOVEN_SCOPED_KEY"),
    kitchen="default"
)

print("=" * 70)
print("DELETING OLD AGENT")
print("=" * 70)
print(f"Agent Name: {config.AGENT_NAME}")
print()

try:
    agent = client.get_agent(config.AGENT_NAME)
    print(f"Found agent: {config.AGENT_NAME}")
    print("Deleting...")
    
    result = client.delete(agent)
    print(result)
    print()
    print("=" * 70)
    print("✅ AGENT DELETED SUCCESSFULLY!")
    print("=" * 70)
    print(f"\nNow run: python create_agent.py")
    print()
    
except Exception as e:
    print(f"[ERROR] {e}")
    import traceback
    traceback.print_exc()
