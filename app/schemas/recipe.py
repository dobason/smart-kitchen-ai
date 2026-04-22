from pydantic import BaseModel
from typing import List, Optional
from .preference import Preference

class RecipeRequest(BaseModel):
    ingredients: List[str]
    preference: Optional[Preference] = None

class RecipeResponse(BaseModel):
    ingredients: List[str] = []
    dish: Optional[str] = None
    steps: List[str] = []
    time: Optional[str] = None