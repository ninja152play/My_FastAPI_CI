from fastapi import FastAPI

from app.database import create_db
from app.recipes.routes import router


async def lifespan(app):
    await create_db()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(router=router)

