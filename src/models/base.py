from uuid import UUID


class Base:
    def __init__(self, pk: UUID) -> None:
        self._id = pk

    @property
    def id(self) -> UUID:
        return self._id
