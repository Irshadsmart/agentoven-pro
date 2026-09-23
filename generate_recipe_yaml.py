"""
Generate recipe.yaml from config.py
This script generates the recipe YAML file from the Python configuration.
Run this after making changes to config.py to update the recipe definition.
"""
import os
import config

# Build the recipe YAML structure
recipe_yaml = f"""# Generated from config.py
# Last Updated: {os.path.basename(__file__)}
# Edit config.py and run: python generate_recipe_yaml.py

name: {config.RECIPE_NAME}
version: {config.RECIPE_VERSION}
description: |
  {config.RECIPE_DESCRIPTION}

metadata:
  author: {config.RECIPE_AUTHOR}
  tags:
    - {', '.join(config.RECIPE_TAGS)}

steps:
  # STEP 1: {config.STEP_1_TITLE}
  - id: {config.STEP_1_ID}
    type: {config.STEP_1_TYPE}
    agent: {config.STEP_1_AGENT}
    title: "{config.STEP_1_TITLE}"
    description: "{config.STEP_1_DESCRIPTION}"
    input:
      prompt: "{config.STEP_1_PROMPT}"

  # STEP 2: {config.STEP_2_TITLE}
  - id: {config.STEP_2_ID}
    type: {config.STEP_2_TYPE}
    agent: {config.STEP_2_AGENT}
    title: "{config.STEP_2_TITLE}"
    description: "{config.STEP_2_DESCRIPTION}"
    input:
      prompt: "{config.STEP_2_PROMPT}"

  # STEP 3: {config.STEP_3_TITLE}
  - id: {config.STEP_3_ID}
    type: {config.STEP_3_TYPE}
    agent: {config.STEP_3_AGENT}
    title: "{config.STEP_3_TITLE}"
    description: "{config.STEP_3_DESCRIPTION}"
    input:
      prompt: "{config.STEP_3_PROMPT}"

  # STEP 4: {config.STEP_4_TITLE} (HUMAN GATE)
  - id: {config.STEP_4_ID}
    type: {config.STEP_4_TYPE}
    title: "{config.STEP_4_TITLE}"
    description: "{config.STEP_4_DESCRIPTION}"
    message: |
      {config.STEP_4_MESSAGE}
    timeout: {config.STEP_4_TIMEOUT}
    actions:
      - id: approve
        label: "Approve"
        description: "Approve the draft and proceed to finalization"
      - id: reject
        label: "Reject"
        description: "Reject the draft and generate summary"

  # STEP 5: {config.STEP_5_TITLE}
  - id: {config.STEP_5_ID}
    type: {config.STEP_5_TYPE}
    agent: {config.STEP_5_AGENT}
    title: "{config.STEP_5_TITLE}"
    description: "{config.STEP_5_DESCRIPTION}"
    input:
      prompt: |
        {{% if steps.human-approval.action == 'approve' %}}
        {config.STEP_5_PROMPT_APPROVED}
        {{% else %}}
        {config.STEP_5_PROMPT_REJECTED}
        {{% endif %}}
"""

# Create recipe folder if it doesn't exist
recipe_folder = config.RECIPE_FOLDER
os.makedirs(recipe_folder, exist_ok=True)

# Write the recipe.yaml file
recipe_yaml_path = os.path.join(recipe_folder, 'recipe.yaml')
with open(recipe_yaml_path, 'w') as f:
    f.write(recipe_yaml)

agentoven_url = os.getenv("AGENTOVEN_URL")

print("=" * 70)
print("RECIPE YAML GENERATED")
print("=" * 70)
print(f"Recipe Name: {config.RECIPE_NAME}")
print(f"Output File: {recipe_yaml_path}")
print(f"Steps: 5")
print()
print("Next steps:")
print(f"  1. Run: python register_recipe.py")
print(f"  2. Run: python run_recipe_workflow.py")
print(f"  3. Open: {agentoven_url}/dishshelf")
print()
