from typing import Self
from uuid import uuid4

from src.mixins.serializable import Serializable

from .entity import Entity


class Category(Entity, Serializable):
    serializable_fields = ('id', 'title')

    @classmethod
    def create(cls, title: str) -> Self:
        return cls(id=uuid4(), title=title)
