# AgentOven 5-Step Recipe with Human Gate - Complete Workflow

## Recipe Overview
The recipe `five-step-human-gate-recipe` has 5 steps:

1. **collect-input** (Agent Step)
   - Collects user input
   - Type: Agent
   - Prompt: "User input: {{input.user_text}}"

2. **analyze** (Agent Step)
   - Analyzes the user's request
   - Type: Agent
   - Input: Takes output from step 1

3. **generate-draft** (Agent Step)
   - Generates a draft response based on analysis
   - Type: Agent
   - Input: Takes output from step 2

4. **human-approval** (Human Gate Step) ⭐ KEY STEP
   - Waits for human decision
   - Type: Human Gate
   - Options: Approve or Reject
   - Status: WAITING (until user clicks button)

5. **finalize** (Agent Step - Conditional)
   - If Approved: Finalizes the response
   - If Rejected: Provides failure summary
   - Type: Agent (Conditional execution)

---

## Step-by-Step Execution Flow

### Step 9-12: Create and Run Recipe

**Option A: Using Python Scripts**
```bash
# Run the recipe
python run_recipe_workflow.py

# Check status
python check_recipe_status.py
```

**Option B: Using AgentOven API directly**
```python
from agentoven import AgentOvenClient

client = AgentOvenClient(
    os.getenv("AGENTOVEN_URL"),
    os.getenv("AGENTOVEN_SCOPED_KEY")
)

# Run recipe with input
result = client.bake_recipe(
    "five-step-human-gate-recipe",
    input='{"user_text": "What is the capital of France?"}'
)
print(result)
```

### Step 13: View in DishShelf UI and Approve/Reject

**Access the UI:**
1. Open browser: `http://localhost:8080/dishshelf`
2. Find "five-step-human-gate-recipe" 
3. Click on the latest run

**What you should see:**
```
Recipe: five-step-human-gate-recipe
Run ID: [uuid]
Status: RUNNING / WAITING

Steps:
  1. collect-input      [✓ COMPLETED]
  2. analyze            [✓ COMPLETED]
  3. generate-draft     [✓ COMPLETED]
  4. human-approval     [⧖ WAITING] ← Waiting for your decision
  5. finalize           [PENDING]
```

**At the human-approval step, you should see:**
```
Title: "Approve or Reject?"
Message: "Please review the draft: [draft output here]"

[APPROVE BUTTON] [REJECT BUTTON]
```

### Step 13 Action: Click Approve

**Click "APPROVE":**

The workflow will continue:
- Step 4 (human-approval) → Status: ✓ COMPLETED (Action: approve)
- Step 5 (finalize) → Executes with approval prompt

**Expected Result:**
```
Steps:
  1. collect-input      [✓ COMPLETED]
  2. analyze            [✓ COMPLETED]
  3. generate-draft     [✓ COMPLETED]
  4. human-approval     [✓ COMPLETED] (Approved)
  5. finalize           [✓ COMPLETED]

Overall Status: COMPLETED ✓
```

### Alternative: Click Reject

**Click "REJECT":**

The workflow will continue:
- Step 4 (human-approval) → Status: ✓ COMPLETED (Action: reject)
- Step 5 (finalize) → Executes with rejection prompt

**Expected Result:**
```
Steps:
  1. collect-input      [✓ COMPLETED]
  2. analyze            [✓ COMPLETED]
  3. generate-draft     [✓ COMPLETED]
  4. human-approval     [✓ COMPLETED] (Rejected)
  5. finalize           [✓ COMPLETED] (with failure summary)

Overall Status: COMPLETED ✓
```

---

## Status Meanings

| Status | Meaning | Color |
|--------|---------|-------|
| COMPLETED | Step finished successfully | Green ✓ |
| RUNNING | Step is currently executing | Blue > |
| WAITING | Waiting for human input | Orange ⧖ |
| PENDING | Queued, not started yet | Gray |
| FAILED | Step encountered error | Red ✗ |

---

## Monitoring Script

Check status at any time:
```bash
python check_recipe_status.py
```

This will show:
- All recipe runs
- Current status of each run
- Status of each step within the run
- Actions taken at human gate

---

## Expected Timeline

1. Recipe starts → Steps 1-3 execute quickly (a few seconds)
2. Step 4 (human-approval) → **PAUSED, WAITING FOR USER**
3. User clicks Approve/Reject in UI
4. Step 5 (finalize) → Executes based on decision
5. Recipe completes → All steps show ✓ COMPLETED

**IMPORTANT:** The status should NEVER be "PAUSED" - it should be "WAITING" or "RUNNING"

---

## Troubleshooting

### Recipe completes too fast without waiting
- Check that the recipe YAML has the `type: human` step
- Verify the human gate step has proper `title`, `message`, and `actions`
- Check DishShelf logs for errors

### Cannot see steps in UI
- Make sure recipe was baked (created) first
- Use `python register_recipe.py` to ensure recipe is created
- Refresh the browser

### Approve/Reject buttons not appearing
- Ensure `actions` are defined in the human gate step
- Each action must have `id` and `label` fields

### Steps show "FAILED" unexpectedly
- Check that agent `hello-agent-final` exists and is baked
- Verify the system prompts are configured correctly
- Check control plane logs

---

## Files Reference

- `register_recipe.py` - Creates/registers the recipe
- `run_recipe_workflow.py` - Runs the recipe with sample input
- `check_recipe_status.py` - Monitors execution status
- `five-step-human-gate-recipe/recipe.yaml` - Recipe definition

---

## Summary

1. ✓ Recipe created with 5 steps (including human gate)
2. ✓ Recipe registered and baked
3. → Run: `python run_recipe_workflow.py`
4. → View: Open DishShelf UI
5. → Approve: Click button in UI
6. → Verify: Run `python check_recipe_status.py`
7. ✓ All steps should show COMPLETED in green
