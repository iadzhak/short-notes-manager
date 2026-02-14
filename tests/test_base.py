import pytest

from uuid import uuid4
from src.models.base import Base


class TestBase:
    id1 = uuid4()
    id2 = uuid4()

    def test_create(self):
        new = Base(self.id1)
        assert new.id == self.id1

    def test_cant_change_id(self):
        new = Base(self.id1)
        with pytest.raises(AttributeError):
            new.id = self.id2
        assert new.id == self.id1
