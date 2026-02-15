from unittest.mock import patch

from datetime import datetime
from uuid import uuid4

from src.models.category import Category
from src.models.note import Note
from src.storage.category_storage import CategoryStorage


class TestSerializable:
    name = 'John'
    age = 25
    note = 'Hello'

    serialized = {
        'name': name,
        'age': age,
    }

    def test_to_dict(self, custom_class):
        new = custom_class(self.name, self.age, self.note)
        assert new.to_dict() == self.serialized

    def test_from_dict(self, custom_class):
        new = custom_class.from_dict(self.serialized)
        assert new.name == self.name
        assert new.age == self.age
        assert new.note is None


class TestCategorySerializable:
    id = uuid4()
    title = 'Some Category'
    category = Category(id, title)
    serialized = {'id': str(id), 'title': title}

    def test_to_dict(self):
        assert self.category.to_dict() == self.serialized

    def test_from_dict(self):
        category = Category.from_dict(self.serialized)
        assert isinstance(category, Category)
        assert category.id == self.category.id
        assert category.title == self.category.title


class TestNoteSerializable:
    id = uuid4()
    title = 'Some Note'
    text = 'Some Text'
    category = Category.create('Some Category')
    created_at = datetime.now()
    serialized = {
        'id': str(id),
        'title': title,
        'text': text,
        'category': str(category.id),
        'created_at': str(created_at)
    }

    def test_to_dict(self):
        note = Note(
            id=self.id,
            title=self.title,
            text=self.text,
            category=self.category,
            created_at=self.created_at
        )
        assert note.to_dict() == self.serialized

    def test_from_dict(self, category_filepath):
        category_storage = CategoryStorage(category_filepath)
        category_storage.data[self.category.id] = self.category
        category_storage.save()
        with patch('src.storage.category_storage.category_storage', category_storage):
            note = Note.from_dict(self.serialized)
            assert note.id == self.id
            assert note.title == self.title
            assert note.text == self.text
            assert note.category == self.category
            assert note.created_at == self.created_at
