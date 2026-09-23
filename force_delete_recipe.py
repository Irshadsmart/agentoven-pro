"""
Force Delete Recipe via REST API
Deletes the recipe from the database so it can be recreated
"""
from agentoven import AgentOvenClient
import os
import config

recipe_name = config.RECIPE_NAME

print("=" * 70)
print("DELETE RECIPE (via REST API)")
print("=" * 70)
print(f"Recipe Name: {recipe_name}")
print()

client = AgentOvenClient(
    os.getenv("AGENTOVEN_URL"),
    os.getenv("AGENTOVEN_SCOPED_KEY")
)

try:
    # Try to delete via REST API endpoint
    print(f"[1] Attempting to delete recipe: {recipe_name}")

    # Try calling internal _delete method with the recipe name
    result = client._delete(f"/recipes/{recipe_name}")

    print(f"    [OK] Recipe deleted!")
    print(f"    Result: {result}")
    print()
    print("=" * 70)
    print("SUCCESS!")
    print("=" * 70)
    print(f"Recipe '{recipe_name}' has been deleted from database.")
    print(f"\nNext: Run python register_recipe.py to recreate it")
    print()

except Exception as e:
    print(f"[ERROR] {e}")
    print()
    print("Note: If error is 404, recipe doesn't exist (which is fine)")
    print("      Just run: python register_recipe.py")
    import traceback
    traceback.print_exc()
