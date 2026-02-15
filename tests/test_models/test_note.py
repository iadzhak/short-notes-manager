import pytest
from datetime import datetime, timedelta
from uuid import UUID

from src.models.note import Note
from src.models.category import Category


class TestNote:
    title = 'test note'
    text = 'test text'
    new_text = 'new test text'
    category = Category.create('test category')

    def create_instance(self):
        return Note.create(self.title, self.text, self.category)

    def test_create(self):
        note = self.create_instance()
        assert note.title == self.title
        assert note.text == self.text
        assert note.category == self.category
        assert isinstance(note.created_at, datetime)
        assert isinstance(note.id, UUID)

    def test_update(self):
        note = self.create_instance()
        note.text = self.new_text
        assert note.text == self.new_text

    def test_cant_change_created_at(self):
        note = self.create_instance()
        new_created_at = note.created_at - timedelta(days=1)
        with pytest.raises(AttributeError):
            note.created_at = new_created_at

    def test_str_repr(self):
        note = self.create_instance()
        str_repr = f'Note(id={note.id}, title={note.title!r}, text={note.text!r}, category={note.category!r}, created_at={note.created_at!r})'
        assert str_repr == str(note)
