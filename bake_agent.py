"""
Bake Agent
Activates the agent so it's ready to use
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
print("BAKING AGENT")
print("=" * 70)
print(f"Agent Name: {config.AGENT_NAME}")
print(f"Environment: {config.AGENT_ENVIRONMENT}")
print()

agent = client.get_agent(config.AGENT_NAME)

print("Baking Agent...")
result = client.bake(agent, environment=config.AGENT_ENVIRONMENT)
print(result)
print()
print("=" * 70)
print("✅ AGENT BAKING STARTED!")
print("=" * 70)
print(f"\n⏳ Wait 20-30 seconds for agent to be READY")
print(f"📍 Check Agents page: {os.getenv('AGENTOVEN_URL')}/agents")
print(f"   Agent '{config.AGENT_NAME}' should show status: READY")
print()
print("When READY, run: python create_recipe.py")
print()
