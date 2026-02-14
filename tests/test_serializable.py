from uuid import uuid4

import pytest

from src.mixins.serializable import Serializable
from src.models.category import Category


class Custom(Serializable):
    serializable_fields = ('name', 'age')

    def __init__(self, name, age, note=None):
        self.name = name
        self.age = age
        self.note = note


class TestSerializable:
    name = 'John'
    age = 25
    note = 'Hello'

    serialized = {
        'name': name,
        'age': age,
    }

    def test_to_dict(self):
        new = Custom(self.name, self.age, self.note)
        assert new.to_dict() == self.serialized

    def test_from_dict(self):
        new = Custom.from_dict(self.serialized)
        assert new.name == self.name
        assert new.age == self.age
        assert new.note is None


class TestCategorySerializable:
    id = uuid4()
    title = 'Some Category'
    category = Category(id, title)
    serialized = {'id': id, 'title': title}

    def test_to_dict(self):
        assert self.category.to_dict() == self.serialized

    def test_from_dict(self):
        category = Category.from_dict(self.serialized)
        assert isinstance(category, Category)
        assert category.id == self.category.id
        assert category.title == self.category.title
