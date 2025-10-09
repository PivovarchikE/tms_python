from classes import Book, Library
from exceptions_my import NotStrException, NotIntException

# create book class
a = Book(500, 1954, "Yanka Lucina", "Homeland", 176)
b = Book(400, 1924, "Aloiza Pashkevich", "Belarusian violin", 17)
c = Book(600, 1923, "Yanka Kupala", "Zhaleika", 295)
d = Book(299, 1926, "Yanka Kupala", "Guslar", 295)
print('--------------------')
try:
    e = Book("299", 1926, "Yanka Kupala", "Guslar", 295)
except NotIntException as er:
    print('1', er)
except NotStrException as er:
    print(er)

try:
    f = Book(299, 1926, 123, 123, 295)
except NotIntException as er:
    print(er)
except NotStrException as er:
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
print('12', lib.get_book_info('Yanka Kupala'))
lib.add_book(a)
print('13', lib.library)
lib.add_book(b)
lib.add_book(c)
lib.add_book(d)
print('14', lib.library)
print('--------------------')
# тест метода получения инфо о книгах с поиском по автору
print('15', lib.get_book_info(''))
print('16', lib.get_book_info('yap'))
print('17', lib.get_book_info(['yap', 'nam']))
print('18', lib.get_book_info('Yanka Kupala'))
print('19', lib.get_book_info(['Yanka Kupala', "Aloiza Pashkevich"]))
# способ вывода через for
print('20')
for book in lib.get_book_info(['Yanka Lucina', "Aloiza Pashkevich"]):
    print(book.book_id, book)
print('--------------------')
print(lib.get_book_info(1))
