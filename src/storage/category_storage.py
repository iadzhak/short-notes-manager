from pathlib import Path

from .csv_storage import CSVStorage
from ..models.category import Category


class CategoryStorage(CSVStorage):
    def __init__(self, filepath: Path, model_class=Category) -> None:
        super().__init__(filepath=filepath, model_class=model_class)

    def all(self) -> list[Category]:
        return list(self.data.values())

    def create(self, title: str) -> Category:
        category = Category.create(title=title)
        self.data[category.id] = category
        self.save()
        return category

    def get_by_title(self, title: str) -> Category | None:
        for category in self.all():
            if category.title == title:
                return category
        return None
