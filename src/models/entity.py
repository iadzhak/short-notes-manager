from uuid import UUID

from .base import Base


class Entity(Base):
    def __init__(self, id: UUID, title: str) -> None:
        super().__init__(id=id)
        self.title = title

    def __str__(self) -> str:
        return f'{self.__class__.__name__}(id={self.id}, title={self.title!r})'

    def __repr__(self) -> str:
        return str(self)
