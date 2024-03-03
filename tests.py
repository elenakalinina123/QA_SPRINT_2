import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Тестовые данные для параметризации тестов
    test_books = [
        ("Book 1", "Фантастика"),
        ("Book 2", "Ужасы"),
        ("Book 3", "Детективы"),
        ("Book 4", "Мультфильмы"),
        ("Book 5", "Комедии"),
        ("Book 6", "Фэнтези"),  # Жанр, отсутствующий в списке genre
    ]

    test_favorites = ["Book 1", "Book 3"]

    # Тесты для метода add_new_book
    # book[0] это первый элемент кортежа (название)
    @pytest.mark.parametrize("name", [book[0] for book in test_books])
    def test_add_new_book(self, name, collector):
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    def test_add_new_book_invalid_name(self, collector):
        # Попытка добавить книгу с недопустимым названием (символов > 40)
        invalid_name = "A" * 41
        collector.add_new_book(invalid_name)
        assert invalid_name not in collector.books_genre

    # Тесты для метода set_book_genre
    def test_set_book_genre(self, collector):
        name, genre = self.test_books[0]
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_set_book_genre_invalid_genre(self, collector):
        # Попытка установить жанр, который отсутствует в списке genre
        name, invalid_genre = self.test_books[5]
        collector.add_new_book(name)
        collector.set_book_genre(name, invalid_genre)
        assert collector.get_book_genre(name) is not invalid_genre

    # Тесты для метода get_book_genre
    def test_get_book_genre(self, collector):
        name, genre = self.test_books[0]
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        assert collector.get_book_genre(name) is genre

        assert collector.get_book_genre('fake name') is None

    # Тесты для метода get_books_with_specific_genre

    def test_get_books_with_specific_genre(self, collector):
        # Добавляем две книги с жанром "Фантастика"

        collector.add_new_book("Book 1")
        collector.set_book_genre("Book 1", "Фантастика")
        collector.add_new_book("Book 2")
        collector.set_book_genre("Book 2", "Ужасы")

        # Получаем список книг с жанром "Фантастика"
        books_with_specific_genre = collector.get_books_with_specific_genre(
            "Фантастика")

        # Проверяем, что список содержит ровно одну книгу
        assert len(books_with_specific_genre) == 1

    def test_get_books_for_children_genre(self, collector):
        # Добавляем две книги с жанром "Фантастика"
        collector.add_new_book("Book 1")
        collector.set_book_genre("Book 1", "Фантастика")

        # Добавляем одну книгу с жанром "Ужасы"
        collector.add_new_book("Book 2")
        collector.set_book_genre("Book 2", "Ужасы")

        # Получаем список книг с жанром "Для детей"
        books_for_children = collector.get_books_for_children()

        # Проверяем, что в списке книг есть книга для детей
        assert "Book 1" in books_for_children

    # разве так лучше?
    def test_get_no_adult_books_for_children_genre(self, collector):
        # Добавляем две книги с жанром "Фантастика"
        collector.add_new_book("Book 1")
        collector.set_book_genre("Book 1", "Фантастика")

        # Добавляем одну книгу с жанром "Ужасы"
        collector.add_new_book("Book 2")
        collector.set_book_genre("Book 2", "Ужасы")

        # Получаем список книг с жанром "Для детей"
        books_for_children = collector.get_books_for_children()

        # Проверяем, что в списке книг для детей нет книг не для детей
        assert "Book 2" not in books_for_children

    # Тест для метода add_book_in_favorites
    def test_add_book_to_favorites(self, collector):
        book_name = self.test_books[0][0]
        collector.add_new_book(book_name)

        collector.add_book_in_favorites(book_name)

        assert len(collector.get_list_of_favorites_books()) == 1

    # Тест для метода add_book_in_favorites повторное добавление
    def test_add_book_to_favorites_repeated(self, collector):
        book_name = self.test_books[0][0]
        collector.add_new_book(book_name)

        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)

        assert len(collector.get_list_of_favorites_books()) == 1

    # Тест для метода delete_book_from_favorites

    def test_delete_book_from_favorites(self, collector):
        book_name = self.test_books[0][0]
        collector.add_new_book(book_name)

        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)

        assert len(collector.get_list_of_favorites_books()) == 0

    # Тест для метода get_list_of_favorites_books

    def test_get_list_of_favorites_books(self, collector):
        for name, genre in self.test_books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        for name in self.test_favorites:
            collector.add_book_in_favorites(name)

        favorites_list = collector.get_list_of_favorites_books()
        assert all(book in favorites_list for book in self.test_favorites)
