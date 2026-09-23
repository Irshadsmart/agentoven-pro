# 🚀 AGENTOVEN WORKFLOW - Complete Step-by-Step Guide

## Summary of Changes
✅ **Fixed the Recipe Issue!** Now using Recipe() and Step() constructors directly (ChatGPT's approach)
✅ **Removed YAML generation** - it wasn't working properly with AgentOven
✅ **Three clean Python files** - create_agent.py, bake_agent.py, create_recipe.py
✅ **Config-driven** - change config.py to create new agents/recipes

---

## 🎯 WORKFLOW - 9 Steps Total

### Step 1: Verify Configuration
**File**: config.py
**Action**: Review these values (can change as needed)
```
AGENT_NAME = "hello-agent-final"
RECIPE_NAME = "approval-workflow-with-human-gate"
RECIPE_DESCRIPTION = "A comprehensive 5-step workflow with human approval gate..."
```

### Step 2: Create Agent
**File**: create_agent.py
**Action**: Run in terminal
```powershell
python create_agent.py
```
**Expected Output**:
```
CREATING AGENT
Agent Name: hello-agent-final
...
✅ AGENT CREATED SUCCESSFULLY!
```

**Then Check in UI**:
📍 Go to: https://agentoven.techdwarfs.com/agents
✓ You should see "hello-agent-final" in the agents list

### Step 3: Bake Agent
**File**: bake_agent.py
**Action**: Run in terminal
```powershell
python bake_agent.py
```
**Expected Output**:
```
BAKING AGENT
Agent Name: hello-agent-final
...
✅ AGENT BAKING STARTED!
⏳ Wait 20-30 seconds for agent to be READY
```

**Then Check in UI**:
📍 Refresh: https://agentoven.techdwarfs.com/agents
⏳ Wait 20-30 seconds
✓ Click on "hello-agent-final"
✓ Status should change from "baking" → "READY"

### Step 4: Verify Agent Works (Optional)
**Action**: Test the agent directly
- Click on agent "hello-agent-final"
- Click "Test" button
- Enter test input: "What is the capital of France?"
- ✓ Should get a response

### Step 5: Create Recipe
**File**: create_recipe.py
**Action**: Run in terminal
```powershell
python create_recipe.py
```
**Expected Output**:
```
CREATING RECIPE
Recipe Name: approval-workflow-with-human-gate
Steps: 5
  1. collect-input
  2. analyze
  3. generate-draft
  4. human-approval
  5. finalize

✅ RECIPE CREATED SUCCESSFULLY!
```

**Then Check in UI**:
📍 Go to: https://agentoven.techdwarfs.com/recipes
✓ You should see "approval-workflow-with-human-gate"
✓ Click on it
✓ **IMPORTANT**: You should now see 5 steps displayed:
   - collect-input
   - analyze
   - generate-draft
   - human-approval (with Approve/Reject buttons)
   - finalize

### Step 6: Run the Recipe
**Action**: In UI, click "Run" button on the recipe

**Enter Test Input**:
```json
{
  "user_text": "Please review this document for quality assurance"
}
```

**Action**: Click "Submit"

**Expected**:
- Recipe execution starts
- You'll see execution ID
- Status shows "running"

### Step 7: Monitor in DishShelf
**Action**: Go to: https://agentoven.techdwarfs.com/dishshelf

**Watch the Workflow**:
- ✓ collect-input (completes)
- ✓ analyze (completes)
- ✓ generate-draft (completes)
- ⏸️ human-approval (waits for your decision)

### Step 8: Approve or Reject
**Action**: In DishShelf, click on "human-approval" step

**Two Scenarios**:

**Scenario A - Approve**:
1. Click "Approve" button
2. Step completes
3. finalize step runs and completes
4. Workflow shows: ✅ ALL STEPS COMPLETED
5. Status: "COMPLETED"

**Scenario B - Reject**:
1. Click "Reject" button
2. Workflow terminates
3. Status: "FAILED"

### Step 9: Done! ✅
You've successfully:
✅ Created an agent
✅ Baked (activated) the agent
✅ Created a 5-step recipe with human gate
✅ Executed the recipe
✅ Approved/Rejected through the human gate
✅ Monitored execution in DishShelf

---

## 🔄 For Tomorrow: Creating a New Agent/Recipe

If you want to create a NEW agent and recipe tomorrow, just:

1. **Update config.py**:
   ```python
   AGENT_NAME = "new-agent-name"
   RECIPE_NAME = "new-recipe-name"
   STEP_1_TITLE = "New Step 1"
   # ... update other step titles as needed
   ```

2. **Run the same commands**:
   ```powershell
   python create_agent.py
   python bake_agent.py
   python create_recipe.py
   ```

3. **Check in UI** (same as above)

**That's it!** The configuration system handles everything.

---

## 📝 Files Reference

| File | Purpose |
|------|---------|
| config.py | Master configuration - MODIFY THIS |
| create_agent.py | Creates agent from config.py |
| bake_agent.py | Activates agent |
| create_recipe.py | Creates recipe with 5 steps |
| run_recipe_workflow.py | (Optional) Run recipe from command line |
| check_recipe_status.py | (Optional) Check execution status |

---

## ⚙️ Environment Variables Required

Make sure these are set in PowerShell:
```powershell
$env:AGENTOVEN_URL = "https://agentoven.techdwarfs.com"
$env:AGENTOVEN_SCOPED_KEY = "your-scoped-key-here"
```

---

## ✨ Key Difference from Before

❌ **OLD (Didn't work)**: 
- Generated recipe.yaml files
- Used Recipe(folder) constructor
- Steps didn't display in UI

✅ **NEW (Works perfectly)**:
- Uses Recipe() constructor with Step() objects directly
- Follows ChatGPT's proven approach
- Steps display correctly in UI
- Human gate works as expected

---

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| "Agent not found" | Wait for bake_agent.py to complete (20-30 seconds) |
| Steps don't show in recipe | Already fixed - use create_recipe.py |
| Human gate not appearing | Make sure recipe was created with create_recipe.py |
| Can't see DishShelf | Use correct URL: https://agentoven.techdwarfs.com/dishshelf |

