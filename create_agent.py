"""
Create Agent
Follows ChatGPT's approach - uses Agent() constructor directly
"""
from agentoven import Agent
from agentoven.client import AgentOvenClient
import os
import config

client = AgentOvenClient(
    url=os.getenv("AGENTOVEN_URL"),
    api_key=os.getenv("AGENTOVEN_SCOPED_KEY"),
    kitchen="default"
)

agent = Agent(
    config.AGENT_NAME,
    description=config.AGENT_DESCRIPTION,
    model_provider=config.AGENT_MODEL_PROVIDER,
    model_name=config.AGENT_MODEL_NAME,
    system_prompt=config.AGENT_SYSTEM_PROMPT
)

print("=" * 70)
print("CREATING AGENT")
print("=" * 70)
print(f"Agent Name: {config.AGENT_NAME}")
print(f"Model: {config.AGENT_MODEL_PROVIDER}/{config.AGENT_MODEL_NAME}")
print()

print("Creating Agent...")
result = client.register(agent)
print(result)
print()
print("=" * 70)
print("✅ AGENT CREATED SUCCESSFULLY!")
print("=" * 70)
print(f"\nNext step: python bake_agent.py")
print()
