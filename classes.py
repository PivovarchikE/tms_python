from dataclasses import dataclass
from exceptions_my import (InvalidPagesValueError, InvalidYearValueError,
                           InvalidAuthorValueError, InvalidNameValueError,
                           InvalidPriceValueError, InvalidValue,
                           EmptyLibraryException, AuthorNotFound)


"""
Библиотека:

- Класс Book:
   Используем dataclass для создания книги.
   Атрибуты: book_id, pages, year, author, price. Book_id по умолчанию None
   присваивается только при добавлении книги в библиотеку.
   Выполняем валидацию атрибутов при создании книги. Для валидации создаем
   собственные исключения
   Реализуем метод сравнения книг по цене.


- Класс Library:
   Хранит книги и автоматически присваивает каждой книге уникальный id.
   Имеет методы add_book и get_book_info.
   Поддерживает метод для поиска книг по автору с перегрузкой: можно искать
   по одному автору или передавать список авторов.

Переопределить методы str в классах для красивого вывода объектов

Примечание: в рамках задания создать два файла: classes.py и main.py.
В первом будут описаны все классы, во втором классы будут импортированы и
использованы.
"""


@dataclass(eq=False, order=False)
class Book:
    pages: int
    year: int
    author: str
    name: str
    price: float
    book_id: int = None

    def __post_init__(self):
        if not isinstance(self.pages, int):
            raise InvalidPagesValueError(self.pages)

        if not isinstance(self.year, int):
            raise InvalidYearValueError(self.year)

        if not isinstance(self.author, str):
            raise InvalidAuthorValueError(self.author)

        if not isinstance(self.name, str):
            raise InvalidNameValueError(self.name)

        if not isinstance(self.price, float):
            raise InvalidPriceValueError(self.price)

    def __str__(self):
        return (f'{self.author}, {self.name}, {self.year} year, '
                f'{self.pages} pages, {self.price} USD')

    def __eq__(self, other):
        return self.price == other.price

    def __ne__(self, other):
        return self.price != other.price

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price


class Library:
    def __init__(self):
        self.books = {}
        self.next_id = 1

    def add_book(self, book):
        book.book_id = self.next_id
        self.next_id += 1
        self.books[book.book_id] = book

    def get_book_info(self, authors):
        if not isinstance(authors, (str, list)):
            raise TypeError(
                "Аргумент authors должен быть строкой или списком строк")

        if not self.books:
            raise EmptyLibraryException

        if not authors:
            raise InvalidValue

        result = [book for book in self.books.values()
                  if book.author in authors]
        if not result:
            raise AuthorNotFound
        else:
            return result

    def __str__(self):
        return '\n'.join(str(book) for book in self.books)
