import pytest
from src.storage.category_storage import CategoryStorage
from src.models.category import Category


@pytest.fixture
def category_storage(category_filepath):
    category_storage = CategoryStorage(filepath=category_filepath)
    return category_storage


class TestCategoryStorage:
    category = Category.create(title='Tetst Category')
    new_title = 'New Category'

    def set_up(self, category_storage):
        category_storage.data[self.category.id] = self.category
        category_storage.save()
        self.reload(category_storage)

    @staticmethod
    def reload(category_storage):
        category_storage.data.clear()
        category_storage.load()

    def test_all(self, category_storage):
        self.set_up(category_storage)
        all_data = category_storage.all()
        assert len(all_data) == 1
        item = all_data[0]
        assert item.id == self.category.id
        assert item.title == self.category.title

    def test_create(self, category_storage):
        self.set_up(category_storage)
        new_item = category_storage.create(title=self.new_title)
        self.reload(category_storage)
        assert new_item.title == self.new_title
        assert len(category_storage.data) == 2

    def test_get_by_title(self, category_storage):
        self.set_up(category_storage)
        search_word = self.category.title
        item = category_storage.get_by_title(search_word)
        assert item.title == search_word
        assert item.id == self.category.id
