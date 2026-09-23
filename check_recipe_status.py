"""
Check Recipe Status and Display Steps
Shows all recipe runs with their step-by-step status
Reads recipe name from config.py
"""
from agentoven import AgentOvenClient
import os
import json
import config

client = AgentOvenClient(
    os.getenv("AGENTOVEN_URL"),
    os.getenv("AGENTOVEN_SCOPED_KEY")
)

recipe_name = config.RECIPE_NAME

print("\n" + "=" * 80)
print("RECIPE EXECUTION STATUS VIEWER")
print("=" * 80)

try:
    # Get all recipe runs
    runs_json = client.get_recipe_runs(recipe_name)
    runs = json.loads(runs_json.strip()) if isinstance(runs_json, str) else runs_json

    if not runs:
        print("\n[!] No recipe runs found yet.")
        print("\nTo start a recipe run, execute:")
        print("  python run_recipe_workflow.py")
        print("\nThen run this script again to check status.")
    else:
        print(f"\n[OK] Found {len(runs)} recipe run(s)\n")

        for idx, run in enumerate(runs, 1):
            run_id = run.get("id", "N/A")
            status = run.get("status", "unknown")
            started = run.get("started_at", "N/A")
            completed = run.get("completed_at")

            status_display = f"STATUS: {status.upper()}"
            print(f"--- Run #{idx} ---")
            print(f"  ID:       {run_id}")
            print(f"  {status_display}")
            print(f"  Started:  {started}")
            if completed:
                print(f"  Completed: {completed}")
            print()

            # Try to get detailed step information
            try:
                run_details_json = client.get_recipe_run(recipe_name, run_id)
                run_details = json.loads(run_details_json) if isinstance(run_details_json, str) else run_details_json

                if "steps" in run_details:
                    print(f"  STEPS:")
                    for step in run_details["steps"]:
                        step_id = step.get("id", "?")
                        step_type = step.get("type", "?")
                        step_status = step.get("status", "?")

                        # Format step type
                        type_label = "[AGENT]" if step_type == "agent" else "[HUMAN]" if step_type == "human" else f"[{step_type.upper()}]"

                        # Format status with visual indicator
                        if step_status == "completed":
                            status_indicator = "[✓ COMPLETED]"
                        elif step_status == "running":
                            status_indicator = "[> RUNNING]"
                        elif step_status == "waiting":
                            status_indicator = "[⧖ WAITING]"
                        elif step_status == "failed":
                            status_indicator = "[✗ FAILED]"
                        else:
                            status_indicator = f"[{step_status.upper()}]"

                        print(f"    {step_id:20} {type_label:8} {status_indicator}")

                        # Show action taken for human gate
                        if step_type == "human" and "action_taken" in step:
                            action = step.get("action_taken")
                            print(f"      → Action: {action}")

                        # Show output if available
                        if "output" in step and step["output"]:
                            output_str = str(step["output"])
                            if len(output_str) > 60:
                                print(f"      → {output_str[:60]}...")
                            else:
                                print(f"      → {output_str}")

            except Exception as e:
                print(f"  [Note] Could not fetch detailed steps: {type(e).__name__}")

            print()

except Exception as e:
    print(f"\n[ERROR] {e}")
    import traceback
    traceback.print_exc()

agentoven_url = os.getenv("AGENTOVEN_URL")

print("=" * 80)
print("VIEW IN UI")
print("=" * 80)
print(f"""
To view and interact with recipe runs in the DishShelf UI:

1. Open your browser and go to:
   {agentoven_url}/dishshelf

2. Find the recipe: {recipe_name}

3. Click on the latest run to see:
   - All 5 steps with their status
   - Human gate approval dialog
   - Options to Approve or Reject

4. Click "Approve" or "Reject" button

5. Re-run this script to see updated status:
   python check_recipe_status.py

Expected workflow:
  collect-input → analyze → generate-draft → [HUMAN GATE] → finalize

After Approval:
  All steps should show [✓ COMPLETED] in green

After Rejection:
  Steps up to finalize should show appropriate status
  Human gate should show [✗ REJECTED]
""")
