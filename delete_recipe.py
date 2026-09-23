"""
Delete Recipe
Deletes the recipe so it can be recreated fresh
"""
from agentoven import AgentOvenClient, Recipe
import os
import config

recipe_name = config.RECIPE_NAME
recipe_folder = config.RECIPE_FOLDER

print("=" * 70)
print("DELETE RECIPE")
print("=" * 70)
print(f"Recipe Name: {recipe_name}")
print()

client = AgentOvenClient(
    os.getenv("AGENTOVEN_URL"),
    os.getenv("AGENTOVEN_SCOPED_KEY")
)

try:
    recipe = Recipe(recipe_folder)
    print(f"[1] Deleting recipe: {recipe_name}")
    result = client.delete(recipe)
    print(f"    [OK] Recipe deleted successfully!")
    print(f"    Result: {result}")
    print()
    print("=" * 70)
    print("SUCCESS!")
    print("=" * 70)
    print(f"Recipe '{recipe_name}' has been deleted.")
    print(f"\nNext steps:")
    print(f"  1. Run: python register_recipe.py")
    print(f"  2. Run: python run_recipe_workflow.py")
    print()

except Exception as e:
    print(f"[ERROR] {e}")
    import traceback
    traceback.print_exc()
