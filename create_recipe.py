"""
Create Recipe
Follows ChatGPT's approach - uses Recipe() and Step() constructors directly
This is the key difference: NOT generating YAML, using Python objects directly
"""
from agentoven import Recipe, Step
from agentoven.client import AgentOvenClient
import os
import config

client = AgentOvenClient(
    url=os.getenv("AGENTOVEN_URL"),
    api_key=os.getenv("AGENTOVEN_SCOPED_KEY"),
    kitchen="default"
)

# Build all 5 steps
steps = [
    Step(
        config.STEP_1_ID,
        agent=config.AGENT_NAME
    ),
    
    Step(
        config.STEP_2_ID,
        agent=config.AGENT_NAME,
        depends_on=[config.STEP_1_ID]
    ),
    
    Step(
        config.STEP_3_ID,
        agent=config.AGENT_NAME,
        depends_on=[config.STEP_2_ID]
    ),
    
    Step(
        config.STEP_4_ID,
        human_gate=True,
        depends_on=[config.STEP_3_ID]
    ),
    
    Step(
        config.STEP_5_ID,
        agent=config.AGENT_NAME,
        depends_on=[config.STEP_4_ID]
    ),
]

recipe = Recipe(
    config.RECIPE_NAME,
    description=config.RECIPE_DESCRIPTION,
    steps=steps
)

print("=" * 70)
print("CREATING RECIPE")
print("=" * 70)
print(f"Recipe Name: {config.RECIPE_NAME}")
print(f"Steps: {len(steps)}")
step_ids = [config.STEP_1_ID, config.STEP_2_ID, config.STEP_3_ID, config.STEP_4_ID, config.STEP_5_ID]
for i, step_id in enumerate(step_ids, 1):
    print(f"  {i}. {step_id}")
print()

print("Creating Recipe...")
result = client.create_recipe(recipe)
print(result)
print()
print("=" * 70)
print("✅ RECIPE CREATED SUCCESSFULLY!")
print("=" * 70)
print(f"\n📍 Check Recipes page: {os.getenv('AGENTOVEN_URL')}/recipes")
print(f"   Recipe '{config.RECIPE_NAME}' should show 5 steps")
print()
print("Next steps:")
print("  1. Click Run button on the recipe")
print("  2. Enter sample input and Submit")
print("  3. Go to DishShelf to monitor execution")
print()
