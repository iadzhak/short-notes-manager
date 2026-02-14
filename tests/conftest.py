from uuid import UUID, uuid4

import pytest
from pathlib import Path
from src.mixins.serializable import Serializable
from src.models.category import Category

CSV_DIR = Path(__file__).parent / 'csv_data'


@pytest.fixture
def custom_class():
    """Для кастомных проверок, без привязки к классам приложения"""

    class Custom(Serializable):
        serializable_fields = ('name', 'age')

        def __init__(self, name, age, note=None, id=None):
            super().__init__()
            self.name = name
            self.age = int(age)
            self.note = note
            if id is not None:
                id = id if isinstance(id, UUID) else UUID(id)
            self.id = id

    return Custom


@pytest.fixture
def custom_filepath():
    path = CSV_DIR / 'custom.csv'
    path.parent.mkdir(parents=True, exist_ok=True)
    yield path
    if path.exists():
        path.unlink()


@pytest.fixture
def category_filepath():
    path = CSV_DIR / 'categories.csv'
    path.parent.mkdir(parents=True, exist_ok=True)
    yield path
    if path.exists():
        path.unlink()
