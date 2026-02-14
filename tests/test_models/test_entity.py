import pytest
from uuid import uuid4

from src.models.entity import Entity


class TestEntity:
    pk = uuid4()
    title = "Test"
    new_title = "New Test"

    def test_create(self):
        new = Entity(id=self.pk, title=self.title)
        assert new.id == self.pk
        assert new.title == self.title

    def test_edit(self):
        new = Entity(id=self.pk, title=self.title)
        new.title = self.new_title
        assert new.title == self.new_title

    def test_str_repr(self):
        new = Entity(id=self.pk, title=self.title)
        assert str(new) == f"Entity(id={self.pk}, title={self.title!r})"
