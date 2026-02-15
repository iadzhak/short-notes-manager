import pytest
from datetime import datetime, timedelta
from uuid import UUID

from src.models.note import Note


class TestNote:
    title = 'test note'
    text = 'test text'
    new_text = 'new test text'

    def test_create(self):
        note = Note.create(self.title, self.text)
        assert note.title == self.title
        assert note.text == self.text
        assert isinstance(note.created_at, datetime)
        assert isinstance(note.id, UUID)

    def test_update(self):
        note = Note.create(self.title, self.text)
        note.text = self.new_text
        assert note.text == self.new_text

    def test_cant_change_created_at(self):
        note = Note.create(self.title, self.text)
        new_created_at = note.created_at - timedelta(days=1)
        with pytest.raises(AttributeError):
            note.created_at = new_created_at

    def test_str_repr(self):
        note = Note.create(self.title, self.text)
        str_repr = f'Note(id={note.id}, title={note.title!r}, text={note.text!r}, created_at={note.created_at!r})'
        assert str_repr == str(note)
