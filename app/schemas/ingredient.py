from pydantic import BaseModel
from typing import List

class ImageObject(BaseModel):
    image_name: str
    presigned_url: str
    bucket_name: str

class IngredientsResponse(BaseModel):
    image_obj: ImageObject
    ingredients: List[str]