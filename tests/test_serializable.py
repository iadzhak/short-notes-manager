from uuid import uuid4

from src.models.category import Category


class TestSerializable:
    name = 'John'
    age = 25
    note = 'Hello'

    serialized = {
        'name': name,
        'age': age,
    }

    def test_to_dict(self, custom_class):
        new = custom_class(self.name, self.age, self.note)
        assert new.to_dict() == self.serialized

    def test_from_dict(self, custom_class):
        new = custom_class.from_dict(self.serialized)
        assert new.name == self.name
        assert new.age == self.age
        assert new.note is None


class TestCategorySerializable:
    id = uuid4()
    title = 'Some Category'
    category = Category(id, title)
    serialized = {'id': id, 'title': title}

    def test_to_dict(self):
        assert self.category.to_dict() == self.serialized

    def test_from_dict(self):
        category = Category.from_dict(self.serialized)
        assert isinstance(category, Category)
        assert category.id == self.category.id
        assert category.title == self.category.title
