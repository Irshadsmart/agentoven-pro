"""
Register & Bake Recipe from CONFIG
Reads recipe name from config.py and registers it with AgentOven
"""
from agentoven import AgentOvenClient, Recipe
import os
import config

recipe_name = config.RECIPE_NAME
recipe_folder = config.RECIPE_FOLDER
environment = config.RECIPE_ENVIRONMENT

print("=" * 70)
print("REGISTERING RECIPE")
print("=" * 70)
print(f"Recipe Name: {recipe_name}")
print(f"Recipe Folder: {recipe_folder}/recipe.yaml")
print(f"Environment: {environment}")
print()

client = AgentOvenClient(
    os.getenv("AGENTOVEN_URL"),
    os.getenv("AGENTOVEN_SCOPED_KEY")
)

try:
    # Load recipe from folder (recipe.yaml must be inside this folder)
    print(f"[1] Loading recipe from: {recipe_folder}/recipe.yaml")
    recipe = Recipe(recipe_folder)
    print(f"    [OK] Recipe loaded")

    # Create/Register recipe
    print(f"[2] Registering recipe: {recipe_name}")
    client.create_recipe(recipe)
    print(f"    [OK] Recipe registered successfully!")

    # Bake recipe
    print(f"[3] Baking recipe for environment: {environment}")
    client.bake(recipe, environment=environment)
    print(f"    [OK] Recipe baked successfully!")

    agentoven_url = os.getenv("AGENTOVEN_URL")

    print()
    print("=" * 70)
    print("SUCCESS!")
    print("=" * 70)
    print(f"Recipe '{recipe_name}' is ready to use.")
    print(f"\nNext steps:")
    print(f"  1. Run: python run_recipe_workflow.py")
    print(f"  2. Open: {agentoven_url}/dishshelf")
    print(f"  3. Find recipe: {recipe_name}")
    print(f"  4. Click 'DishShelf' to view execution")
    print()

except Exception as e:
    print()
    print("=" * 70)
    print("ERROR!")
    print("=" * 70)
    print(f"[ERROR] {e}")
    print()
    if "duplicate" in str(e).lower():
        print("Note: Recipe already exists (this is ok)")
        print("You can run: python run_recipe_workflow.py")
    import traceback
    traceback.print_exc()
