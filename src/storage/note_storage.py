from pathlib import Path

from .csv_storage import CSVStorage
from ..models.note import Note
from ..models.category import Category
from ..settings import NOTE_STORAGE_FILEPATH


class NoteStorage(CSVStorage):
    def __init__(self, filepath: Path, model_class=Note):
        super().__init__(filepath=filepath, model_class=model_class)

    def create(self, title: str, text: str, category: Category) -> Note:
        note = Note.create(
            title=title,
            text=text,
            category=category
        )
        self.data[note.id] = note
        self.save()
        return note

    def get_by_category(self, category: Category) -> list[Note]:
        return [n for n in self.all() if n.category.id == category.id]


note_storage = NoteStorage(NOTE_STORAGE_FILEPATH)
note_storage.load()
