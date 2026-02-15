from typing import ClassVar, Any, Self, TYPE_CHECKING


class Serializable:
    serializable_fields: ClassVar[tuple[str, ...]] = ()

    if TYPE_CHECKING:
        def __init__(self, *args, **kwargs): ...

    def _serialize_field(self, field: str) -> str:
        if serialize := getattr(self, f'serialize_{field}', None):
            return serialize()
        return getattr(self, field, None)

    def to_dict(self) -> dict[str, Any]:
        data = {}
        for field in self.serializable_fields:
            data[field] = self._serialize_field(field)
        return data

    @classmethod
    def _deserialize_field(cls, field: str, value: Any) -> Any:
        if deserialize := getattr(cls, f'deserialize_{field}', None):
            return deserialize(value)
        return value

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        for field in data:
            data[field] = cls._deserialize_field(field, data[field])
        return cls(**data)
