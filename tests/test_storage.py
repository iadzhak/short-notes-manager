from uuid import uuid4

import pytest

from src.storage.csv_storage import CSVStorage


class TestCSVStorage:
    id = uuid4()
    name = 'test'
    age = 20

    def test_save(self, custom_class, custom_filepath):
        custom_class.serializable_fields = ('name', 'age', 'id')
        storage = CSVStorage(filepath=custom_filepath, model_class=custom_class)
        new = custom_class(name=self.name, age=self.age)
        new.id = self.id
        storage.data[new.id] = new
        storage.save()
        line1 = 'name,age,id\n'
        line2 = f'{new.name},{new.age},{new.id}\n'
        with open(custom_filepath, 'r') as f:
            assert f.readline() == line1
            assert f.readline() == line2

    def test_load(self, custom_class, custom_filepath):
        with open(custom_filepath, 'w') as f:
            f.write('id,name,age\n')
            f.write(f'{self.id},{self.name},{self.age}')
        storage = CSVStorage(filepath=custom_filepath, model_class=custom_class)
        storage.load()
        assert self.id in storage.data
        item = storage.data[self.id]
        assert isinstance(item, custom_class)
        assert item.id == self.id
        assert item.name == self.name
        assert item.age == self.age
