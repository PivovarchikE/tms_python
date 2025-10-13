from classes import Book, Library
from exceptions_my import (InvalidPagesValueError, InvalidAuthorValueError,
                           InvalidValue, EmptyLibraryException, AuthorNotFound)


# create book class
a = Book(500, 1954, "Yanka Lucina", "Homeland", 176.00)
b = Book(400, 1924, "Aloiza Pashkevich", "Belarusian violin", 17.00)
c = Book(600, 1923, "Yanka Kupala", "Zhaleika", 295.00)
d = Book(299, 1926, "Yanka Kupala", "Guslar", 295.00)
print('--------------------')

try:
    e = Book("299", 1926, "Yanka Kupala", "Guslar", 295.00)
except InvalidPagesValueError as er:
    print('1', er)

try:
    f = Book(299, 1926, 123, "123", 295.00)
except InvalidAuthorValueError as er:
    print('2', er)


print('--------------------')
print('3', a, b, c, d, sep='\n')
print('--------------------')
# test comparison operators
print('4', a > b)
print('5', a >= b)
print('6', c >= d)
print('7', a < b)
print('8', a <= b)
print('9', c <= d)
print('10', a == b)
print('11', c == d)
print('--------------------')

# library class
lib = Library()
try:
    print('12', lib.get_book_info('Yanka Kupala'))
except EmptyLibraryException as e:
    print(e)
lib.add_book(a)
print('13', lib.books)
lib.add_book(b)
lib.add_book(c)
lib.add_book(d)
print('14', lib.books)
print('--------------------')
# тест метода получения инфо о книгах с поиском по автору
try:
    print('15', lib.get_book_info(''))
except InvalidValue:
    print('Подано пустое значение')
try:
    print('16', lib.get_book_info('yap'))
except AuthorNotFound as e:
    print(e)
print('17', lib.get_book_info('Yanka Kupala'))
print('18', lib.get_book_info(['Yanka Kupala', "Aloiza Pashkevich"]))
# способ вывода через for
print('19')
for book in lib.get_book_info(['Yanka Lucina', "Aloiza Pashkevich"]):
    print(book.book_id, book)
print('--------------------')
print(lib.get_book_info(1))
