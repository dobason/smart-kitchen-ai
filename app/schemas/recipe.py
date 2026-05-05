from pydantic import BaseModel
from typing import List, Optional
from .preference import Preference


class RecipeIngredientItem(BaseModel):
    """Một nguyên liệu gồm tên và lượng dùng."""
    name: str
    amount: str


class RecipeRequest(BaseModel):
    ingredients: List[str]
    preference: Optional[Preference] = None


class RecipeResponse(BaseModel):
    """
    Schema phản hồi mới từ Gemini.
    - name: Tên món ăn
    - ingredients: Danh sách nguyên liệu kèm lượng dùng
    - steps: Các bước nấu theo thứ tự
    """
    name: Optional[str] = None
    ingredients: List[RecipeIngredientItem] = []
    steps: List[str] = []
    time: Optional[str] = None