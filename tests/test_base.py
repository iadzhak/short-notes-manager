import pytest

from uuid import uuid4
from src.models.base import Base


class TestBase:

    def test_create(self):
        pk = uuid4()
        new = Base(pk)
        assert new.id == pk

    def test_cant_change_id(self):
        pk1 = uuid4()
        pk2 = uuid4()
        new = Base(pk1)
        with pytest.raises(AttributeError):
            new.id = pk2
        assert new.id == pk1
