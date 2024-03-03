Для тестирования класса BooksCollector был использован фреймворк pytest. В проекте реализовано 9 тестов, которые покрывают различные сценарии использования 
методов класса.

1. `test_add_new_book`:
   - Проверяет, что метод `add_new_book` корректно добавляет новую книгу в словарь `books_genre` без указания жанра.
   
2. `test_add_new_book_invalid_name`:
   - Проверяет, что нельзя добавить книгу с недопустимым названием (символов > 40).

3. `test_set_book_genre`:
   - Проверяет, что метод `set_book_genre` устанавливает жанр книге, если книга есть в `books_genre` и её жанр входит в список `genre`.
   - Проверяет, что нельзя установить жанр, который отсутствует в списке `genre`.

4. `test_set_book_genre_invalid_genre`:
   - Проверяет, что метод `set_book_genre` не изменяет жанр книги, если указанный жанр отсутствует в списке `genre`.
  
5. `test_get_book_genre`:
   - Проверяет, что метод `get_book_genre` выдает жанр книги
  
6. `test_get_books_with_specific_genre`:
   - Проверяет, что метод `get_books_with_specific_genre` возвращает список книг с определённым жанром.
  
7. `test_get_books_for_children_genre`:
   - Проверяет, что метод `get_books_for_children` возвращает книги, которые подходят детям (жанр книги в списке `genre_age_rating`).

8. `test_get_no_adult_books_for_children_genre`:
    - Проверяет, что метод `get_books_for_children` не возвращает книги, которые не подходят детям (жанр книги отсутствует в списке `genre_age_rating`).


9. `test_add_book_to_favorites`:
   - Проверяет что метод `add_book_to_favorites` добавляет книгу в список избранного.

10. `test_add_book_to_favorites_repeated`:
   - Проверяет что метод `add_book_to_favorites` добавляет книгу в список избранного второй раз.

11. `test_delete_book_from_favorites`:
   - Проверяет что метод `delete_book_to_favorites` удаляет книгу из списка избранного.

12. `test_get_list_of_favorites_books`:
    - Проверяет, что метод `get_list_of_favorites_books` выдает список книг в избранном.