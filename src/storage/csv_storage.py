from os import write
from pathlib import Path
from uuid import UUID
from csv import DictReader, DictWriter

from .base import StorageProtocol
from ..models.base import HasId
from ..mixins.serializable import Serializable


class CSVStorage[T: Serializable | HasId](StorageProtocol):

    def __init__(self, filepath: Path, model_class: type[T]):
        self.filepath = filepath
        self.model_class = model_class
        self.data: dict[UUID, T] = {}

    def save(self) -> None:
        self.filepath.parent.mkdir(parents=True, exist_ok=True)
        with self.filepath.open('w') as f:
            writer = DictWriter(
                f, fieldnames=self.model_class.serializable_fields
            )
            writer.writeheader()
            writer.writerows(
                item.to_dict()
                for item in self.data.values()
            )

    def load(self) -> None:
        if not self.filepath.exists():
            return
        with self.filepath.open('r') as f:
            reader = DictReader(f)
            for row in reader:
                entity = self.model_class.from_dict(row)
                self.data[entity.id] = entity
