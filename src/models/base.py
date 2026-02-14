from uuid import UUID


class Base:
    def __init__(self, id: UUID) -> None:
        self._id = id

    @property
    def id(self) -> UUID:
        return self._id
