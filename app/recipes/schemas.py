from typing import Optional

from pydantic import BaseModel


class SRecipesList(BaseModel):
    title: str
    cooking_time: int
    views: int


class SRecipe(BaseModel):
    title: str
    cooking_time: int
    ingredients: str
    description: Optional[str] = None
