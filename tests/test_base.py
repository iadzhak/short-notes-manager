import pytest

from uuid import uuid4
from src.models.base import Base


class TestBase:
    pk1 = uuid4()
    pk2 = uuid4()

    def test_create(self):
        new = Base(self.pk1)
        assert new.id == self.pk1

    def test_cant_change_id(self):
        new = Base(self.pk1)
        with pytest.raises(AttributeError):
            new.id = self.pk2
        assert new.id == self.pk1
