from google import genai
from typing import Optional
from app.core.config import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

async def generate_recipe_from_ingredients(ingredients: list[str], preferences: dict, lang: Optional[str] = "en") -> str:
    prompt = f"""
    You are a cooking assistant.

    Ingredients:
    {ingredients}

    Preferences:
    {preferences}

    Task:
    - Suggest best matching dish
    - Provide clear recipe
    - Keep it practical
    - Response in language {lang}

    Return JSON:
    {{
        "dish": "",
        "ingredients": [],
        "steps": [],
        "time": ""
    }}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt)

    return response.text