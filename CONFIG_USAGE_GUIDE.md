# Configuration System - Complete Guide

## Overview

All agent and recipe configuration is now centralized in **`config.py`**. This means:

✅ Change one file → All scripts automatically use new values  
✅ Create new agents/recipes → Just modify `config.py`  
✅ No hardcoded values → Everything is configurable  
✅ Easy to maintain → Single source of truth  

---

## File Structure

```
agentoven-project/
├── config.py                          ← MASTER CONFIGURATION FILE
├── generate_recipe_yaml.py            ← Generates recipe.yaml from config.py
├── register_recipe.py                 ← Uses config.py
├── run_recipe_workflow.py             ← Uses config.py
├── check_recipe_status.py             ← Uses config.py
│
├── five-step-human-gate-recipe/
│   └── recipe.yaml                    ← Generated from config.py
│
└── (other scripts...)
```

---

## How It Works

### 1. Configuration (config.py)
Define all values here:
```python
AGENT_NAME = "hello-agent-final"
RECIPE_NAME = "five-step-human-gate-recipe"
STEP_1_TITLE = "Collect User Input"
# ... etc
```

### 2. Generate YAML (generate_recipe_yaml.py)
Creates recipe.yaml from config.py:
```bash
python generate_recipe_yaml.py
```
This generates: `five-step-human-gate-recipe/recipe.yaml`

### 3. Register Recipe (register_recipe.py)
Reads config and registers with AgentOven:
```bash
python register_recipe.py
```
Automatically uses values from `config.py`

### 4. Run Recipe (run_recipe_workflow.py)
Executes the recipe:
```bash
python run_recipe_workflow.py
```
Automatically uses values from `config.py`

---

## Creating a New Recipe Tomorrow

### Simple 3-Step Process:

#### Step 1: Update config.py

Open `config.py` and change these values:

```python
# Change agent name if using a different agent
AGENT_NAME = "new-agent-name"

# Change recipe name
RECIPE_NAME = "my-new-recipe"
RECIPE_FOLDER = "my-new-recipe"  # Must match the folder name
RECIPE_DESCRIPTION = "Description of my new recipe"

# Update step titles and prompts
STEP_1_TITLE = "Step 1 new title"
STEP_1_PROMPT = "New prompt for step 1"
# ... etc for other steps
```

#### Step 2: Generate Recipe YAML

```bash
python generate_recipe_yaml.py
```

This creates:
- Folder: `my-new-recipe/`
- File: `my-new-recipe/recipe.yaml` (auto-generated from config.py)

#### Step 3: Register and Run

```bash
python register_recipe.py
python run_recipe_workflow.py
```

That's it! All scripts automatically use the new configuration.

---

## Example: Creating a Document Review Recipe

### Before (in config.py)

```python
RECIPE_NAME = "five-step-human-gate-recipe"
RECIPE_DESCRIPTION = "A 5-step workflow with human approval gate..."

STEP_1_TITLE = "Collect User Input"
STEP_3_TITLE = "Generate Draft"
STEP_4_TITLE = "Human Approval Review"
```

### After (updated config.py)

```python
RECIPE_NAME = "document-review-pipeline"
RECIPE_DESCRIPTION = "Document review pipeline with validation, analysis, and human approval..."

STEP_1_TITLE = "Collect Document"
STEP_3_TITLE = "Generate Review Report"
STEP_4_TITLE = "Reviewer Approval"
```

### Then run:

```bash
python generate_recipe_yaml.py
python register_recipe.py
python run_recipe_workflow.py
```

New recipe is ready! ✅

---

## Configuration Variables Reference

### Agent Configuration
| Variable | Purpose | Example |
|----------|---------|---------|
| `AGENT_NAME` | Agent to use for steps | `"hello-agent-final"` |
| `AGENT_DESCRIPTION` | Agent description | `"Friendly assistant"` |
| `AGENT_MODEL_PROVIDER` | LLM provider | `"my-openai"` |
| `AGENT_MODEL_NAME` | Model name | `"gpt-5"` |
| `AGENT_SYSTEM_PROMPT` | Agent instructions | `"You are..."` |
| `AGENT_ENVIRONMENT` | Deployment environment | `"Prod"` |

### Recipe Configuration
| Variable | Purpose | Example |
|----------|---------|---------|
| `RECIPE_NAME` | Recipe name | `"five-step-human-gate-recipe"` |
| `RECIPE_FOLDER` | Folder name | `"five-step-human-gate-recipe"` |
| `RECIPE_DESCRIPTION` | Full description | `"A 5-step workflow..."` |
| `RECIPE_AUTHOR` | Author name | `"AgentOven Team"` |
| `RECIPE_ENVIRONMENT` | Deployment environment | `"Prod"` |
| `RECIPE_TAGS` | Tags for organization | `["human-gate", "approval"]` |

### Step Configuration (5 Steps)
Each step has configurable fields:

#### Step 1-3 (Agent Steps)
```python
STEP_X_ID = "step-id"
STEP_X_TYPE = "agent"
STEP_X_TITLE = "Step Title"
STEP_X_DESCRIPTION = "Step description"
STEP_X_AGENT = AGENT_NAME
STEP_X_PROMPT = "Prompt for the agent"
```

#### Step 4 (Human Gate)
```python
STEP_4_ID = "human-approval"
STEP_4_TYPE = "human_gate"
STEP_4_TITLE = "Human Approval"
STEP_4_DESCRIPTION = "Description"
STEP_4_MESSAGE = "Message to reviewer"
STEP_4_TIMEOUT = 3600  # seconds
```

#### Step 5 (Conditional Agent)
```python
STEP_5_ID = "finalize"
STEP_5_TYPE = "agent"
STEP_5_AGENT = AGENT_NAME
STEP_5_PROMPT_APPROVED = "If approved..."
STEP_5_PROMPT_REJECTED = "If rejected..."
```

---

## Workflow

```
┌─────────────────────────────────────────────────────┐
│ 1. Edit config.py                                   │
│    Change RECIPE_NAME, STEP titles, etc.            │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────┐
│ 2. Run generate_recipe_yaml.py                      │
│    python generate_recipe_yaml.py                   │
│    Creates: recipe-name/recipe.yaml                 │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────┐
│ 3. Run register_recipe.py                           │
│    python register_recipe.py                        │
│    Registers with AgentOven                         │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────┐
│ 4. Run run_recipe_workflow.py                       │
│    python run_recipe_workflow.py                    │
│    Executes the recipe                              │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────┐
│ 5. View in DishShelf                                │
│    http://localhost:8080/dishshelf                  │
│    Click Approve/Reject                             │
└──────────────┬──────────────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────────────┐
│ 6. Check status                                     │
│    python check_recipe_status.py                    │
│    View final results                               │
└─────────────────────────────────────────────────────┘
```

---

## Quick Commands

```bash
# Generate recipe.yaml from config.py
python generate_recipe_yaml.py

# Register recipe
python register_recipe.py

# Run recipe with sample input
python run_recipe_workflow.py

# Check execution status
python check_recipe_status.py

# View in browser
http://localhost:8080/dishshelf
```

---

## Common Modifications

### Change Agent Used
```python
# Change from:
AGENT_NAME = "hello-agent-final"

# To:
AGENT_NAME = "my-custom-agent"
```

### Add More Steps to Recipe
Edit config.py to add additional STEP_6, STEP_7, etc. (careful: recipe expects 5 steps, may need custom logic)

### Modify Step Prompts
```python
# Change from:
STEP_2_PROMPT = "Analyze and understand this request: {{steps.collect-input.output}}"

# To:
STEP_2_PROMPT = "Your custom prompt: {{steps.collect-input.output}}"
```

### Modify Human Gate Message
```python
# Change from:
STEP_4_MESSAGE = "Please review the following draft..."

# To:
STEP_4_MESSAGE = "Please review and approve/reject this document..."
```

---

## Important Notes

1. **RECIPE_NAME must match RECIPE_FOLDER** - They must be the same:
   ```python
   RECIPE_NAME = "my-recipe"
   RECIPE_FOLDER = "my-recipe"  # Same name!
   ```

2. **Always run generate_recipe_yaml.py after config changes** - This ensures recipe.yaml is updated:
   ```bash
   python generate_recipe_yaml.py
   ```

3. **Recipe must already exist if re-registering** - It's ok to get "duplicate key" error, just run the workflow:
   ```bash
   python run_recipe_workflow.py
   ```

4. **Template variables are available**:
   - `{{input.user_text}}` - User input
   - `{{steps.step-id.output}}` - Output from previous step
   - `{{steps.human-approval.action}}` - User's approval action

---

## Troubleshooting

### Recipe shows "0 steps" in UI
1. ✅ Edit config.py
2. ✅ Run `python generate_recipe_yaml.py`
3. ✅ Run `python register_recipe.py`
4. ✅ Refresh browser

### Recipe.yaml not updating
```bash
# Always regenerate after config changes
python generate_recipe_yaml.py
```

### Scripts use old values
```bash
# Clear Python cache
rm -rf __pycache__

# Regenerate everything
python generate_recipe_yaml.py
python register_recipe.py
```

---

## Examples for Tomorrow

### Customer Support Recipe
```python
RECIPE_NAME = "customer-support-pipeline"
RECIPE_FOLDER = "customer-support-pipeline"
AGENT_NAME = "support-agent"

STEP_1_TITLE = "Classify Support Request"
STEP_2_TITLE = "Analyze Customer Issue"
STEP_3_TITLE = "Generate Solution"
STEP_4_TITLE = "Support Manager Approval"
STEP_5_TITLE = "Send Response to Customer"
```

### Content Moderation Recipe
```python
RECIPE_NAME = "content-moderation-workflow"
RECIPE_FOLDER = "content-moderation-workflow"
AGENT_NAME = "content-moderator"

STEP_1_TITLE = "Extract Content"
STEP_2_TITLE = "Analyze Content Safety"
STEP_3_TITLE = "Generate Moderation Report"
STEP_4_TITLE = "Moderator Review"
STEP_5_TITLE = "Apply Moderation Decision"
```

### Data Analysis Recipe
```python
RECIPE_NAME = "data-analysis-pipeline"
RECIPE_FOLDER = "data-analysis-pipeline"
AGENT_NAME = "data-analyst"

STEP_1_TITLE = "Load Data"
STEP_2_TITLE = "Analyze Data Patterns"
STEP_3_TITLE = "Generate Report"
STEP_4_TITLE = "Analyst Approval"
STEP_5_TITLE = "Publish Results"
```

---

## Summary

✅ **Single configuration file** (`config.py`)  
✅ **Generates recipe YAML** (`generate_recipe_yaml.py`)  
✅ **All scripts use config** (register, run, check)  
✅ **Easy to modify** for new recipes  
✅ **Maintainable** - no hardcoded values  
✅ **Ready for production** use  

**To create a new recipe:**
1. Edit `config.py`
2. Run `python generate_recipe_yaml.py`
3. Run `python register_recipe.py`
4. Run `python run_recipe_workflow.py`

Done! 🚀
