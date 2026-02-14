import pytest
from uuid import UUID

from src.models.category import Category


class TestCategory:
    title1 = 'Some category'
    title2 = 'New name category'

    def test_create(self):
        new = Category.create(title=self.title1)
        assert new.title == self.title1
        assert isinstance(new.id, UUID)

    def test_edit(self):
        new = Category.create(title=self.title1)
        assert new.title == self.title1
        new.title = self.title2
        assert new.title == self.title2

    def test_str_repr(self):
        new = Category.create(title=self.title1)
        assert str(new) == f'Category(id={new.id}, title={self.title1!r})'
