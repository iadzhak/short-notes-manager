from uuid import uuid4

import pytest

from src.mixins.serializable import Serializable
from src.models.category import Category


@pytest.fixture
def custom_class():
    """Для кастомных проверок, без привязки к классам приложения"""

    class Custom(Serializable):
        serializable_fields = ('name', 'age')

        def __init__(self, name, age, note=None):
            super().__init__()
            self.name = name
            self.age = age
            self.note = note

    return Custom
