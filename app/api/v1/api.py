from fastapi import APIRouter
from app.api.v1.recipe import router as recipe_router

api = APIRouter()
api.include_router(recipe_router, prefix="/recipe")