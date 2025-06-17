from typing import Annotated, List

from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from ..database import get_db
from .repository import create_recipe_orm, get_recipe_orm, get_recipes_orm
from .schemas import SRecipe, SRecipesList

router = APIRouter()


@router.get("/recipes", response_model=List[SRecipesList])
async def get_recipes(
    session: Annotated[AsyncSession, Depends(get_db)]
) -> List[SRecipesList]:
    return await get_recipes_orm(session)


@router.get("/recipes/{recipe_id}", response_model=SRecipe)
async def get_recipe(
    recipe_id, session: Annotated[AsyncSession, Depends(get_db)]
) -> SRecipe:
    return await get_recipe_orm(session, recipe_id)


@router.post("/recipes")
async def create_recipe(
    recipe: SRecipe, session: Annotated[AsyncSession, Depends(get_db)]
):
    id = await create_recipe_orm(session, recipe)
    return {"recipe_id": id}
