from time import time
from random import randint
from functools import reduce

# 1.
print(list(map(lambda x: str(x), [1, 2, 3])))


# 2.
print(list(filter(lambda x: x > 0, [-1, 0, 1, 2, 3])))

# 3.
print(list(filter(lambda x: x == x[::-1], ['123321', 'aba', 'aab', 'aba',
                                           'avbbva', 'abccba'])))


# 4.
# время считаем в секундах и дельту выводим также
def calculate_time_spent(input_func):

    def wrapper():
        time_start = time()
        input_func()
        time_end = time()
        delta_time = time_end - time_start
        return delta_time
    return wrapper


# длительность времени регулируем изменением правой границы в range
@calculate_time_spent
def generate_list():
    [randint(1, 999999) for _ in range(1, 1000000)]
    return None


print("Затраченное время на выполнение функции generate list в секундах",
      generate_list())


# 5.
rooms = [
            {"name": "Kitchen", "length": 6, "width": 4},
            {"name": "Room 1", "length": 5.5, "width": 4.5},
            {"name": "Room 2", "length": 5, "width": 4},
            {"name": "Room 3", "length": 7, "width": 6.3},
]

square = reduce(lambda accumulate, room:
                accumulate + room.get('length') * room.get('width'), rooms, 0)
print(f"Площадь квартиры = {square}")
