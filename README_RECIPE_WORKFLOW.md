# AgentOven 5-Step Human Gate Recipe - Complete Implementation

## ✅ What Was Done

### Issue Fixed
- **Error**: `register_recipe.py` was using wrong API method
- **Solution**: Updated to use `client.create_recipe()` instead of `client.register()`

### Recipe Created
A complete 5-step recipe with human approval gate:
1. **collect-input** (Agent) - Gets user input
2. **analyze** (Agent) - Analyzes the input
3. **generate-draft** (Agent) - Creates a draft response
4. **human-approval** (Human Gate) - ⭐ Waits for Approve/Reject
5. **finalize** (Agent) - Finalizes or rejects based on decision

### Files Created
- ✅ `register_recipe.py` (FIXED) - Register & bake recipe
- ✅ `run_recipe_workflow.py` (NEW) - Execute recipe with input
- ✅ `check_recipe_status.py` (NEW) - Monitor execution
- ✅ Documentation files (guides, summaries)

---

## 🚀 How to Use (Complete Workflow)

### Step 1: Register the Recipe
```bash
python register_recipe.py
```
Expected output:
```
Recipe registered successfully!
Recipe baked successfully!
```

### Step 2: Run the Recipe
```bash
python run_recipe_workflow.py
```
Expected output:
```
[OK] Recipe already exists (continuing)
[OK] Recipe started!
     Result: {"poll":"/api/v1/recipes/...", "run_id":"...", "status":"running"}
[OK] Found recipe runs:
```

### Step 3: View in DishShelf UI
Open your browser:
```
http://localhost:8080/dishshelf
```

You should see:
- Recipe: `five-step-human-gate-recipe`
- Latest run with all 5 steps
- Steps 1-3 showing ✓ COMPLETED
- Step 4 (human-approval) showing ⧖ WAITING

### Step 4: Approve or Reject
Click one of the buttons at Step 4:
- **[APPROVE]** - Continue to finalization
- **[REJECT]** - Skip to failure summary

### Step 5: Verify Completion
```bash
python check_recipe_status.py
```

Expected output:
```
--- Run #1 ---
  ID:       326d1915-7747-49dc-8a74-bfa6670eae4d
  STATUS: COMPLETED
  
  STEPS:
    collect-input        [AGENT]   [✓ COMPLETED]
    analyze              [AGENT]   [✓ COMPLETED]
    generate-draft       [AGENT]   [✓ COMPLETED]
    human-approval       [HUMAN]   [✓ COMPLETED]
      → Action: approve
    finalize             [AGENT]   [✓ COMPLETED]
```

---

## 📋 Recipe YAML Definition

Located at: `five-step-human-gate-recipe/recipe.yaml`

```yaml
name: five-step-human-gate-recipe
description: A 5-step workflow with Human Gate approval.

steps:
  - id: collect-input
    type: agent
    agent: hello-agent-final
    input:
      prompt: "User input: {{input.user_text}}"

  - id: analyze
    type: agent
    agent: hello-agent-final
    input:
      prompt: "Analyze the user's request: {{steps.collect-input.output}}"

  - id: generate-draft
    type: agent
    agent: hello-agent-final
    input:
      prompt: "Generate a draft response based on analysis: {{steps.analyze.output}}"

  - id: human-approval
    type: human
    title: "Approve or Reject?"
    message: "Please review the draft: {{steps.generate-draft.output}}"
    actions:
      - id: approve
        label: "Approve"
      - id: reject
        label: "Reject"

  - id: finalize
    type: agent
    agent: hello-agent-final
    when:
      - condition: "{{steps.human-approval.action == 'approve'}}"
        input:
          prompt: "Human approved. Finalize the response: {{steps.generate-draft.output}}"
      - condition: "{{steps.human-approval.action == 'reject'}}"
        input:
          prompt: "Human rejected. Marking workflow as failed. Provide failure summary."
```

---

## 🔍 Understanding the Recipe

### Step 1: collect-input
- **Type**: Agent
- **Function**: Receives user input parameter
- **Input**: User text (e.g., "What is the capital of France?")
- **Output**: Agent's understanding of the input

### Step 2: analyze
- **Type**: Agent
- **Function**: Analyzes what the user is asking
- **Input**: Output from step 1
- **Output**: Analysis of the request

### Step 3: generate-draft
- **Type**: Agent
- **Function**: Creates a draft response
- **Input**: Output from step 2
- **Output**: Draft response to the user's request

### Step 4: human-approval ⭐ CRITICAL
- **Type**: Human Gate (BLOCKS execution)
- **Function**: Shows draft and waits for human decision
- **Display**: 
  - Title: "Approve or Reject?"
  - Message: Shows the draft from step 3
  - Buttons: [APPROVE] [REJECT]
- **Behavior**: 
  - Pauses recipe execution
  - Waits for user to click a button
  - Continues based on user action

### Step 5: finalize
- **Type**: Agent (Conditional)
- **Function**: Executes based on approval decision
- **If Approved**: Finalizes and completes the response
- **If Rejected**: Provides a failure summary
- **Output**: Final response or failure message

---

## 🎨 UI Status Indicators

When viewing in DishShelf:

```
STEP STATUS COLORS:
  🟢 GREEN   - COMPLETED (success)
  🔵 BLUE    - RUNNING   (in progress)
  🟠 ORANGE  - WAITING   (needs human input)
  ⚪ GRAY    - PENDING   (not started)
  🔴 RED     - FAILED    (error occurred)
```

---

## ⏱️ Expected Execution Timeline

```
Time    Event
────────────────────────────────────────────────────
0s      Recipe starts
        └─ Step 1: collect-input starts
~2s     Step 1 completes
        └─ Step 2: analyze starts
~5s     Step 2 completes
        └─ Step 3: generate-draft starts
~9s     Step 3 completes
        └─ Step 4: human-approval starts
        │ (⧖ WAITING for human decision)
        │
?s      User clicks button in DishShelf
        └─ Step 5: finalize starts
~11s    Step 5 completes
        └─ Recipe finished (✓ COMPLETED)
```

---

## 🔧 Troubleshooting

### Issue: Recipe completes without showing human gate
**Solution**: 
- Verify recipe YAML has `type: human` for step 4
- Check that actions have `id` and `label`
- Run `python register_recipe.py` again

### Issue: Cannot see UI at localhost:8080
**Solution**:
- Check AGENTOVEN_URL environment variable
- Verify control plane is running
- Check firewall settings

### Issue: Steps show FAILED status
**Solution**:
- Verify agent `hello-agent-final` exists
- Check it's baked in Prod environment
- Review control plane logs

### Issue: Status shows PAUSED instead of WAITING
**Solution**:
- This shouldn't happen with correct recipe
- Reload the DishShelf page
- Check recipe YAML syntax

---

## 📚 Documentation Files

| File | Purpose |
|------|---------|
| `QUICK_START.md` | Fast reference for running workflow |
| `WORKFLOW_GUIDE.md` | Detailed step-by-step guide |
| `FIX_SUMMARY.md` | Visual diagrams of the fix |
| `README_RECIPE_WORKFLOW.md` | This file - complete overview |

---

## ✨ Key Features

✅ **5-Step Recipe**: Complete workflow with multiple agent steps  
✅ **Human Gate**: Step 4 waits for human decision  
✅ **Visual Feedback**: Colors show status in UI  
✅ **Conditional Logic**: Step 5 branches based on approval  
✅ **Full Traceability**: See all steps and outputs  
✅ **No Paused State**: Status is WAITING or RUNNING, never PAUSED  
✅ **Approve/Reject**: Clear action buttons in UI  
✅ **Completion**: All steps show COMPLETED in green  

---

## 📝 Sample Execution

```
INPUT: "What is the capital of France?"

STEP 1 (collect-input): 
  Output: "User is asking about the capital of France"

STEP 2 (analyze):
  Output: "This is a geography question about European capitals"

STEP 3 (generate-draft):
  Output: "The capital of France is Paris. It is located in the 
           north-central part of the country and is the largest city 
           in France. Paris is famous for landmarks like the Eiffel 
           Tower, Notre-Dame, and the Louvre Museum."

STEP 4 (human-approval):
  Title: "Approve or Reject?"
  Message: [Shows above draft]
  → USER CLICKS: [APPROVE]

STEP 5 (finalize):
  Output: "Final response finalized. The draft has been approved."

RESULT: Recipe completes with all steps showing ✓ COMPLETED
```

---

## 🎯 Success Criteria

Your workflow is complete when:

1. ✅ Recipe registered without errors
2. ✅ Recipe runs with sample input
3. ✅ DishShelf shows all 5 steps
4. ✅ Step 4 shows human approval dialog
5. ✅ Clicking Approve/Reject works
6. ✅ Step 5 executes after decision
7. ✅ All steps show COMPLETED in green
8. ✅ Recipe status shows COMPLETED (not PAUSED)
9. ✅ Can run check_recipe_status.py and see results

---

## 🚀 Next Steps

1. **If not done yet**:
   ```bash
   python register_recipe.py
   ```

2. **Run the recipe**:
   ```bash
   python run_recipe_workflow.py
   ```

3. **View in UI**:
   - Open: http://localhost:8080/dishshelf
   - Click: Latest run
   - See: All 5 steps

4. **Approve/Reject**:
   - Click the button at step 4
   - Wait for step 5 to complete

5. **Verify**:
   ```bash
   python check_recipe_status.py
   ```

**You're all set! The 5-step human gate recipe is ready to use.** 🎉

---

## 💡 Quick Commands Reference

```bash
# Register & bake recipe
python register_recipe.py

# Run recipe with input
python run_recipe_workflow.py

# Check execution status
python check_recipe_status.py

# View in browser
open http://localhost:8080/dishshelf
# or on Windows
start http://localhost:8080/dishshelf
```

---

## 📞 Support

For more details, see:
- `QUICK_START.md` - Fast reference
- `WORKFLOW_GUIDE.md` - Complete guide
- `FIX_SUMMARY.md` - Visual explanations
- Recipe YAML: `five-step-human-gate-recipe/recipe.yaml`

Happy baking! 🏺
