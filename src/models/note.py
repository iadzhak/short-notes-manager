from typing import Self
from uuid import UUID, uuid4
from datetime import datetime

from .category import Category
from .entity import Entity
from ..mixins.serializable import Serializable


class Note(Serializable, Entity):
    serializable_fields = ('id', 'title', 'text', 'category', 'created_at')

    def __init__(self, id: UUID, title: str, text: str, category: Category, created_at: datetime) -> None:
        Entity.__init__(self, id=id, title=title)
        self.text = text
        self.category = category
        self._created_at = created_at

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @classmethod
    def create(cls, title: str, text: str, category: Category) -> Self:
        return cls(
            id=uuid4(),
            title=title,
            text=text,
            category=category,
            created_at=datetime.now(),
        )

    @classmethod
    def deserialize_created_at(cls, value: str) -> datetime:
        return datetime.fromisoformat(value)

    def serialize_category(self) -> str:
        return str(self.category.id)

    def serialize_created_at(self) -> str:
        return str(self.created_at)

    @classmethod
    def deserialize_category(cls, value: str) -> Category:
        from ..storage.category_storage import category_storage
        return category_storage.data[UUID(value)]

    def __str__(self) -> str:
        return (
            f'{self.__class__.__name__}(id={self.id}, title={self.title!r},'
            f' text={self.text!r}, category={self.category!r}, created_at={self.created_at!r})'
        )

    def __repr__(self) -> str:
        return str(self)
