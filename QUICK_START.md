# Quick Start - 5-Step Recipe with Human Gate

## Summary of Fix

The issue was in `register_recipe.py` - it was using the wrong API method to register the recipe.

**Problem:** 
- Used `client.register(recipe)` → Expected Agent, got Recipe
- Used `client.bake(recipe, environment="Prod")` → Wrong for recipe creation

**Solution:**
- Use `client.create_recipe(recipe)` to register the recipe
- Use `client.bake(recipe, environment="Prod")` to deploy it

---

## Complete Workflow (Steps 9-15)

### Step 9: Register & Bake Recipe
```bash
python register_recipe.py
```

Output:
```
Recipe registered successfully!
Recipe baked successfully!
```

### Step 10-12: Run Recipe & Verify Entry
```bash
python run_recipe_workflow.py
```

This will:
- Run the recipe with sample input
- Create an execution entry in DishShelf
- Show the run ID

### Step 13: View in UI & Approve/Reject

**Open DishShelf:**
```
http://localhost:8080/dishshelf
```

**Find the recipe run and click to view:**
- You'll see all 5 steps
- Steps 1-3 will show ✓ COMPLETED
- Step 4 (human-approval) will show ⧖ WAITING
- Click **APPROVE** or **REJECT** button

### Step 14-15: Verify Completion

**Check status:**
```bash
python check_recipe_status.py
```

**Expected Result (After Approval):**
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

## Files

| File | Purpose | Status |
|------|---------|--------|
| `register_recipe.py` | Register & bake recipe | ✓ FIXED |
| `five-step-human-gate-recipe/recipe.yaml` | Recipe definition with 5 steps | ✓ OK |
| `run_recipe_workflow.py` | Run recipe with sample input | ✓ CREATED |
| `check_recipe_status.py` | Monitor execution status | ✓ CREATED |
| `WORKFLOW_GUIDE.md` | Detailed workflow guide | ✓ CREATED |

---

## The 5 Steps in Your Recipe

1. **collect-input** (Agent)
   - Accepts user input
   
2. **analyze** (Agent)
   - Analyzes the user's request
   
3. **generate-draft** (Agent)
   - Generates a draft response
   
4. **human-approval** (Human Gate) ← User clicks Approve/Reject here
   - Shows the draft for review
   - Waits for human decision
   
5. **finalize** (Agent)
   - If Approved: Finalizes the response
   - If Rejected: Provides failure summary

---

## Color Indicators in UI

- 🟢 **GREEN** - Completed ✓
- 🔵 **BLUE** - Running >
- 🟠 **ORANGE** - Waiting ⧖
- 🔴 **RED** - Failed ✗

After user clicks "Approve":
- All 5 steps turn 🟢 **GREEN**
- Status shows: **COMPLETED**

After user clicks "Reject":
- Steps 1-4 turn 🟢 **GREEN**
- Step 5 shows status based on rejection handling
- Status shows: **COMPLETED** (not PAUSED)

---

## Key Points

✓ Recipe is created with correct 5 steps  
✓ Human gate step waits for approval  
✓ Approve/Reject buttons appear in UI  
✓ Steps show completed in green after decision  
✓ Status never becomes "PAUSED"  
✓ Full execution visible in DishShelf  

---

## Next Steps

1. Run: `python register_recipe.py` (if not done yet)
2. Run: `python run_recipe_workflow.py`
3. Open: `http://localhost:8080/dishshelf`
4. Click: **APPROVE** or **REJECT**
5. Verify: `python check_recipe_status.py`

Done! 🎉
