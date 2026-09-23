"""
Master Automation Script - Complete Workflow
Creates agent, bakes it, creates recipe, runs recipe, monitors for approval
"""
import subprocess
import time
import os
import json
import sys
import config
from agentoven.client import AgentOvenClient

print("=" * 80)
print("🚀 MASTER AUTOMATION - COMPLETE WORKFLOW")
print("=" * 80)

# Initialize client
client = AgentOvenClient(
    url=os.getenv("AGENTOVEN_URL"),
    api_key=os.getenv("AGENTOVEN_SCOPED_KEY"),
    kitchen="default"
)

# ============================================================================
# STEP 1: CREATE AGENT
# ============================================================================
print("\n[STEP 1/5] Creating Agent...")
print(f"Agent Name: {config.AGENT_NAME}")
try:
    result = subprocess.run(["python", "create_agent.py"], capture_output=True, text=True, timeout=30)
    if result.returncode == 0:
        print("✅ Agent created successfully!")
    else:
        print(f"❌ Error creating agent:\n{result.stderr}")
        sys.exit(1)
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)

# ============================================================================
# STEP 2: BAKE AGENT
# ============================================================================
print("\n[STEP 2/5] Baking Agent (activating)...")
try:
    result = subprocess.run(["python", "bake_agent.py"], capture_output=True, text=True, timeout=30)
    if result.returncode == 0:
        print("✅ Agent baking started!")
        print("⏳ Waiting 30 seconds for agent to be READY...")
        time.sleep(30)
        print("✅ Agent should now be READY!")
    else:
        print(f"❌ Error baking agent:\n{result.stderr}")
        sys.exit(1)
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)

# ============================================================================
# STEP 3: CREATE RECIPE
# ============================================================================
print("\n[STEP 3/5] Creating Recipe with 5 steps...")
print(f"Recipe Name: {config.RECIPE_NAME}")
try:
    result = subprocess.run(["python", "create_recipe.py"], capture_output=True, text=True, timeout=30)
    if result.returncode == 0:
        print("✅ Recipe created successfully!")
    else:
        print(f"❌ Error creating recipe:\n{result.stderr}")
        sys.exit(1)
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)

# ============================================================================
# STEP 4: RUN RECIPE WITH INPUT
# ============================================================================
print("\n[STEP 4/5] Running Recipe with sample input...")

# Sample input
sample_input = {
    "user_text": "Release product documentation v3.0 to production. Needs QA and Product Manager approval. Timeline is this Friday."
}

print(f"Input: {json.dumps(sample_input, indent=2)}")
print(f"Environment: Production (Prod)")

try:
    print("⏳ Executing recipe...")
    result = client.bake_recipe(
        config.RECIPE_NAME,
        environment="Prod",
        input=sample_input
    )
    
    execution_id = result.get("id") or result.get("execution_id") or str(result)
    print(f"✅ Recipe execution started!")
    print(f"Execution ID: {execution_id}")
    
except Exception as e:
    print(f"❌ Error running recipe: {e}")
    sys.exit(1)

# ============================================================================
# STEP 5: MONITOR & WAIT FOR APPROVAL
# ============================================================================
print("\n[STEP 5/5] Monitoring DishShelf for approval...")
print(f"📍 Go to: {os.getenv('AGENTOVEN_URL')}/dishshelf")
print(f"Recipe: {config.RECIPE_NAME}")
print("\n⏳ Waiting for human approval at human-approval step...")
print("   The workflow will execute:")
print("   1. collect-input ✓")
print("   2. analyze ✓")
print("   3. generate-draft ✓")
print("   4. finalize ✓")
print("   5. human-approval ← WAITING FOR YOUR DECISION")
print("\n📌 ACTION REQUIRED:")
print(f"   1. Open: {os.getenv('AGENTOVEN_URL')}/dishshelf")
print(f"   2. Find workflow: {config.RECIPE_NAME}")
print(f"   3. Click 'human-approval' step")
print("   4. Click 'Approve' or 'Reject'")
print("\nPress ENTER when you have approved/rejected in DishShelf...")
input()

print("\n" + "=" * 80)
print("✅ WORKFLOW COMPLETE!")
print("=" * 80)
print(f"\n📊 Summary:")
print(f"   Agent: {config.AGENT_NAME} ✅")
print(f"   Recipe: {config.RECIPE_NAME} ✅")
print(f"   Execution: Complete ✅")
print(f"   Status: Awaiting your approval/rejection in DishShelf ⏳")
print(f"\n📍 Check final results at:")
print(f"   {os.getenv('AGENTOVEN_URL')}/dishshelf")
print()
