from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine("sqlite+aiosqlite:///app.db", echo=True)

new_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_db():
    async with new_session() as session:
        yield session


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
