# название
# время готовки
# список ингредиентов
# текстовое описание
from pydantic import BaseModel
from typing import Optional


class SRecipesList(BaseModel):
    title: str
    cooking_time: int
    views: int


class SRecipe(BaseModel):
    title: str
    cooking_time: int
    ingredients: str
    description: Optional[str] = None