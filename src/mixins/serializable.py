from typing import ClassVar, Any, Self, TYPE_CHECKING


class Serializable:
    serializable_fields: ClassVar[tuple[str, ...]] = ()

    if TYPE_CHECKING:
        def __init__(self, *args, **kwargs): ...

    def to_dict(self) -> dict[str, Any]:
        data = {}
        for field in self.serializable_fields:
            data[field] = getattr(self, field)
        return data

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(**data)
