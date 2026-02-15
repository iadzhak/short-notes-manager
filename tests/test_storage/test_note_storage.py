import pytest
from unittest.mock import patch

from src.storage.note_storage import NoteStorage
from src.storage.category_storage import CategoryStorage
from src.models.note import Note
from src.models.category import Category


@pytest.fixture
def note_storage(note_filepath):
    note_storage = NoteStorage(note_filepath)
    return note_storage


class TestNoteStorage:
    category = Category.create('test_category')
    note = Note.create('title', 'text...', category)

    def setup(self, note_storage, category_filepath):
        category_storage = CategoryStorage(category_filepath)
        category_storage.data[self.category.id] = self.category
        category_storage.save()
        with patch('src.storage.category_storage.category_storage', category_storage):
            note_storage.data[self.note.id] = self.note
            note_storage.save()
            note_storage.data.clear()
            note_storage.load()
            return note_storage

    def test_all(self, note_storage, category_filepath):
        self.setup(note_storage, category_filepath)
        assert len(note_storage.all()) == 1

    def test_get_by_title(self, note_storage, category_filepath):
        self.setup(note_storage, category_filepath)
        item = note_storage.get_by_title(self.note.title)
        assert item.id == self.note.id
        assert item.title == self.note.title
        assert item.text == self.note.text
        assert item.category.id == self.note.category.id
        assert item.created_at == self.note.created_at

    def test_create(self, note_storage):
        note = note_storage.create('title', 'text..', self.category)
        assert len(note_storage.all()) == 1
        assert note.title == 'title'
        assert note.category.id == self.category.id

    def test_get_by_category(self, note_storage, category_filepath):
        self.setup(note_storage, category_filepath)
        data = note_storage.get_by_category(self.category)
        assert len(data) == 1
        assert data[0].category.id == self.category.id
