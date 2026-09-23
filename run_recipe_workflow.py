"""
Complete workflow: Bake Recipe → Run Recipe → Monitor Execution
Reads recipe name from config.py
"""
from agentoven import AgentOvenClient, Recipe
import os
import time
import json
import config

client = AgentOvenClient(
    os.getenv("AGENTOVEN_URL"),
    os.getenv("AGENTOVEN_SCOPED_KEY")
)

recipe_name = config.RECIPE_NAME

# Step 9: Bake Recipe
print("=" * 60)
print("Step 9: BAKE RECIPE")
print("=" * 60)
try:
    recipe = Recipe(recipe_name)
    bake_result = client.bake(recipe, environment="Prod")
    print("[OK] Recipe baked successfully!")
    print(f"     Result: {bake_result}")
except RuntimeError as e:
    if "duplicate" in str(e).lower():
        print("[OK] Recipe already exists (continuing)")
    else:
        print(f"[ERROR] Error baking recipe: {e}")
except Exception as e:
    print(f"[ERROR] Error baking recipe: {e}")

# Step 10: Run Recipe
print("\n" + "=" * 60)
print("Step 10: RUN RECIPE")
print("=" * 60)
try:
    run_input = {
        "user_text": "What is the capital of France?"
    }
    run_result = client.bake_recipe(recipe_name, input=json.dumps(run_input))
    print("[OK] Recipe started!")
    print(f"     Result: {run_result}")
    run_id = run_result if isinstance(run_result, str) else run_result.get("id", "unknown")
except Exception as e:
    print(f"[ERROR] Error running recipe: {e}")
    run_id = None

# Step 11: Verify DishShelf Entry
print("\n" + "=" * 60)
print("Step 11: VERIFY DISHSHELF ENTRY")
print("=" * 60)
try:
    runs = client.get_recipe_runs(recipe_name)
    print("[OK] Found recipe runs:")
    print(json.dumps(runs, indent=2))
except Exception as e:
    print(f"[ERROR] Error fetching recipe runs: {e}")

# Step 12: Verify Waiting Approval (Human Gate)
print("\n" + "=" * 60)
print("Step 12: VERIFY WAITING APPROVAL (HUMAN GATE)")
print("=" * 60)
if run_id:
    try:
        run_details = client.get_recipe_run(recipe_name, run_id)
        print("[OK] Recipe run details:")
        print(json.dumps(run_details, indent=2))

        if "status" in run_details:
            status = run_details["status"]
            print(f"\n     Current Status: {status}")
            if "waiting" in status.lower() or "approval" in status.lower():
                print("[OK] Recipe is waiting for human approval!")

    except Exception as e:
        print(f"[ERROR] Error fetching run details: {e}")
else:
    print("[WARNING] No run ID available. Skipping detailed status check.")

agentoven_url = os.getenv("AGENTOVEN_URL")

print("\n" + "=" * 60)
print("WORKFLOW STATUS")
print("=" * 60)
print(f"""
The recipe is now running with a Human Gate step. To complete steps 13-15:

Step 13: CLICK APPROVE (in UI)
- Navigate to DishShelf UI
- Find the recipe run waiting for approval
- Click the 'Approve' button

Step 14: VERIFY COMPLETED
- The run should transition to 'Completed' status
- Check the final output in the UI

Step 15: ENSURE STATUS NEVER BECOMES 'PAUSED'
- Monitor the execution status
- It should remain 'Running' until the human approves, then become 'Completed'

View the recipe execution in the UI at:
{agentoven_url}/dishshelf
""")
