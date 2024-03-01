Для тестирования класса BooksCollector был использован фреймворк pytest. В проекте реализовано 9 тестов, которые покрывают различные сценарии использования 
методов класса.

1. `test_add_new_book`:
   - Проверяет, что метод `add_new_book` корректно добавляет новую книгу в словарь `books_genre` без указания жанра.
   - Также проверяет, что нельзя добавить книгу с недопустимым названием (символов > 40).

2. `test_set_book_genre`:
   - Проверяет, что метод `set_book_genre` устанавливает жанр книге, если книга есть в `books_genre` и её жанр входит в список `genre`.
   - Проверяет, что нельзя установить жанр, который отсутствует в списке `genre`.

3. `test_set_book_genre_invalid_genre`:
   - Проверяет, что метод `set_book_genre` не изменяет жанр книги, если указанный жанр отсутствует в списке `genre`.
  
4. `test_get_book_genre`:
   - Проверяет, что метод `get_book_genre` выдает жанр книги
  
5. `test_get_books_with_specific_genre`:
   - Проверяет, что метод `get_books_with_specific_genre` возвращает список книг с определённым жанром.
  
6. `test_get_books_for_children_genre`:
   - Проверяет, что метод `get_books_for_children` возвращает книги, которые подходят детям (жанр книги отсутствует в списке `genre_age_rating`).

9. `test_add_and_delete_book_from_favorites`:
   - Проверяет, что методы `add_book_in_favorites` и `delete_book_from_favorites` корректно добавляют и удаляют книги в/из списка избранных.

10. `test_get_list_of_favorites_books`:
    - Проверяет, что метод `get_list_of_favorites_books` выдает список книг в избранном.