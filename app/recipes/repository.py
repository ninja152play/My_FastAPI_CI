from sqlalchemy import select

from .models import Recipe


async def create_recipe_orm(session, recipe):
    obj = Recipe(**recipe.dict())
    session.add(obj)
    await session.flush()
    await session.commit()
    return obj.id


async def get_recipes_orm(session):
    res = await session.execute(select(Recipe))
    recipes = res.scalars().all()
    for r in recipes:
        r.views += 1
    await session.commit()
    return recipes


async def get_recipe_orm(session, recipe_id):
    res = await session.execute(select(Recipe).filter(Recipe.id == recipe_id))
    recipe = res.scalar_one()
    recipe.views += 1
    await session.commit()
    return recipe
