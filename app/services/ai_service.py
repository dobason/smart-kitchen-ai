from app.intergrations.vision_client import detect_ingredients_from_image
from app.intergrations.gemini_client import generate_recipe_from_ingredients
from app.utils.parser import extract_json


async def process_image(file_bytes: bytes, preferences: dict):
    # STEP 1: Detect ingredients
    ingredients = detect_ingredients_from_image(file_bytes)

    if not ingredients:
        return {
            "error": "No food ingredients detected",
            "ingredients": []
        }

    # STEP 2: Generate recipe
    raw = await generate_recipe_from_ingredients(
        ingredients=ingredients,
        preferences=preferences
    )

    recipe = extract_json(raw)

    return {
        "ingredients_detected": ingredients,
        "recipe": recipe
    }