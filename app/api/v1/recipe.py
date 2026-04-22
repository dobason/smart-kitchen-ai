from uuid import uuid4
from asyncio import get_event_loop
from functools import partial

from fastapi import APIRouter, UploadFile, Header


from app.intergrations.minio_client import upload_file
from app.intergrations.vision_client import detect_ingredients_from_image
from app.intergrations.gemini_client import generate_recipe_from_ingredients
from app.schemas.recipe import RecipeRequest, RecipeResponse
from app.schemas.ingredient import IngredientsResponse
from app.utils.parser import extract_json

router = APIRouter()


# get language from header Accept-Language, default to "en"
@router.post("/ingredients", response_model=IngredientsResponse)
async def get_ingredients(
    file: UploadFile,
    lang: str = Header(default="en", alias="Accept-Language")
):

    content = await file.read()
    object_name = f"{uuid4()}.jpg"
    loop = get_event_loop()
    image_obj = await loop.run_in_executor(None, partial(upload_file, content, object_name))

    raw = await detect_ingredients_from_image(image_obj.presigned_url, lang)
    ingredients = [i.strip() for i in raw.split(",") if i.strip()]

    return IngredientsResponse(image_obj=image_obj, ingredients=ingredients)


@router.post("/instruction", response_model=RecipeResponse)
async def get_instruction(
    body: RecipeRequest,
    lang: str = Header(default="en", alias="Accept-Language")
    ):
    preferences = body.preference.model_dump() if body.preference else {}
    raw = await generate_recipe_from_ingredients(body.ingredients, preferences, lang)
    data = extract_json(raw)

    return RecipeResponse(
        dish=data.get("dish"),
        ingredients=data.get("ingredients", []),
        steps=data.get("steps", []),
        time=data.get("time"),
    )
