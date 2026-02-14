from typing import Self
from uuid import uuid4

from .entity import Entity


class Category(Entity):
    @classmethod
    def create(cls, title: str) -> Self:
        return cls(id=uuid4(), title=title)
