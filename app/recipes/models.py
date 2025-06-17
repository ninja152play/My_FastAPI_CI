from sqlalchemy.orm import Mapped, mapped_column

from ..database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    cooking_time: Mapped[int]
    ingredients: Mapped[str]
    description: Mapped[str] = mapped_column(nullable=True)
    views: Mapped[int] = mapped_column(default=0)
