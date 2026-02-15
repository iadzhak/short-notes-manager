from uuid import UUID


class HasId:
    id: UUID


class Base(HasId):
    def __init__(self, id: UUID | str) -> None:
        self._id = id if isinstance(id, UUID) else UUID(id)

    @property
    def id(self) -> UUID:
        return self._id

    def serialize_id(self) -> str:
        return str(self.id)
