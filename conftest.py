import pytest
from main import BooksCollector


# Фикстура, создающая новый экземпляр BooksCollector перед каждым тестом
@pytest.fixture
def collector():
    return BooksCollector()
