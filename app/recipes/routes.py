from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from typing import List

from .schemas import *
from ..database import get_db
from .repository import *


router = APIRouter()


@router.get("/recipes", response_model=List[SRecipesList])
async def get_recipes(
        session: AsyncSession = Depends(get_db)
) -> List[SRecipesList]:
    recipes = await get_recipes_orm(session)
    return recipes



@router.get("/recipes/{recipe_id}", response_model=SRecipe)
async def get_recipe(recipe_id,
                     session: AsyncSession = Depends(get_db)
                     ) -> SRecipe:
    recipe = await get_recipe_orm(session, recipe_id)
    return recipe


@router.post("/recipes")
async def create_recipe(
        recipe: SRecipe,
        session: AsyncSession = Depends(get_db)
):
    id = await create_recipe_orm(session, recipe)
    return {"recipe_id": id}