from pathlib import Path

from ..settings import CATEGORY_STORAGE_FILEPATH
from .csv_storage import CSVStorage
from ..models.category import Category


class CategoryStorage(CSVStorage):
    def __init__(self, filepath: Path, model_class=Category) -> None:
        super().__init__(filepath=filepath, model_class=model_class)

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


category_storage = CategoryStorage(CATEGORY_STORAGE_FILEPATH)
category_storage.load()
