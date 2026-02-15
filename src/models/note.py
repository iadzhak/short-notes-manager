from typing import Self
from uuid import UUID, uuid4
from datetime import datetime

from .entity import Entity


class Note(Entity):
    def __init__(self, id: UUID, title: str, text: str, created_at: datetime) -> None:
        super().__init__(id=id, title=title)
        self.text = text
        self._created_at = created_at

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @classmethod
    def create(cls, title: str, text: str) -> Self:
        return cls(
            id=uuid4(),
            title=title,
            text=text,
            created_at=datetime.now(),
        )

    def __str__(self) -> str:
        return (
            f'{self.__class__.__name__}(id={self.id}, title={self.title!r},'
            f' text={self.text!r}, created_at={self.created_at!r})'
        )

    def __repr__(self) -> str:
        return str(self)
