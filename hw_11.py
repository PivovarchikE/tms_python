"""
1. Создать класс Car. Атрибуты: марка, модель, год  выпуска, скорость
(по умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость  - 5), стоп (сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные.
"""


class Car:

    def __init__(self, brand, model, year_of_production, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year_of_production = year_of_production
        self.__speed = speed

    def increase_speed(self):
        self.__speed += 5

    def decrease_speed(self):
        self.__speed -= 5

    def stop(self):
        self.__speed = 0
    """
    Вопрос. Если атрибуты приватные, я могу их в принте выводить наружу?
    Или приватность касается только изменения атрибутов?
    """
    def display_speed(self):
        print(f'The current speed of the car {self.__brand} {self.__model} ='
              f' {self.__speed}')

    def turn(self):
        self.__speed = -self.__speed


car_1 = Car(brand='Toyota', model='Supra', year_of_production='2007')
car_2 = Car(brand='Toyota', model='Celica', year_of_production='2000')

car_1.display_speed()
car_2.display_speed()
car_1.increase_speed()
car_1.display_speed()
car_1.increase_speed()
car_1.display_speed()
car_2.increase_speed()
car_2.display_speed()
car_1.stop()
car_1.display_speed()
car_2.turn()
car_2.display_speed()

"""
2. Создать класс MyTime. Атрибуты: hours, minutes, seconds.
Методы: переопределить магические методы сравнения(==, !=, >=, <=, <, >),
сложения, вычитания, умножения на число, вывод на экран. Перегрузить
конструктор на обработку входных параметров вида: одна строка, три числа,
другой объект класса MyTime, и отсутствие входных параметров. Реализовать
нормальное отображение времени(12:65:83 - 13:06:23)
"""


class MyTime:

    def __init__(self, *args):
        if len(args) == 0:
            # вариант 4 = отсутствие входных данных
            self.hours = 0
            self.minutes = 0
            self.seconds = 0
        elif len(args) == 1:
            arg = args[0]
            if isinstance(arg, str):
                # вариант 1 = одна строка в формате "HH:MM:SS"
                time_list = arg.strip().split(":")
                if len(time_list) != 3:
                    raise ValueError("Строка должна быть в формате 'HH:MM:SS'")
                else:
                    h = int(time_list[0])
                    m = int(time_list[1])
                    s = int(time_list[2])
                self.hours = h
                self.minutes = m
                self.seconds = s
            elif isinstance(arg, MyTime):
                self.hours = int(arg.hours)
                self.minutes = int(arg.minutes)
                self.seconds = int(arg.seconds)
            else:
                raise ValueError("На вход ожидалась строка в формате "
                                 "'HH:MM:SS' или объект типа MyClass")
        elif len(args) == 3:
            h, m, s = args
            if (not isinstance(h, int) or not isinstance(m, int) or
                    not isinstance(s, int)):
                raise ValueError("На вход ожидались только целые числа")
            else:
                self.hours = int(h)
                self.minutes = int(m)
                self.seconds = int(s)
        else:
            raise ValueError("Некорректное количество входных параметров")

        self._normalize()

    """
    здесь нет контроля часов > 24, т.к. можно
    использовать класс для расчёта длительности
    """
    def _normalize(self):
        # Переводим все в секунды
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds

        # Обрабатываем отрицательные значения
        if total_seconds < 0:
            total_seconds = 0

        # Нормализуем время (остаток от деления на 24 часа)
        self.hours = (total_seconds // 3600) % 24
        self.minutes = (total_seconds % 3600) // 60
        self.seconds = total_seconds % 60

    def __str__(self):
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'

    """
    Определяет поведение оператора равенства, ==
    равенство в пределах одного часа
    """
    def __eq__(self, other):
        return self.hours == other.hours

    """
    Определяет поведение оператора неравенства, !=.
    неравенство, если часы разные
    """
    def __ne__(self, other):
        return self.hours != other.hours

    """
    Определяет поведение оператора меньше, <.
    если часы меньше
    """
    def __lt__(self, other):
        return self.hours < other.hours

    """
    Определяет поведение оператора больше, >.
    если часы больше
    """
    def __gt__(self, other):
        return self.hours > other.hours

    """
    Определяет поведение оператора меньше или равно, <=.
    если часы меньше либо равны
    """
    def __le__(self, other):
        return self.hours <= other.hours

    """
    Определяет поведение оператора больше или равно, >=
    если часы больше либо равны
    """
    def __ge__(self, other):
        return self.hours >= other.hours

    """
    # Сложение.
    h + h, m + m, s + s
    """
    def __add__(self, other):
        h = self.hours + other.hours
        m = self.minutes + other.minutes
        s = self.seconds + other.seconds
        return MyTime(h, m, s)
    """
    # Вычитание.
    h - h, m  - m, s - s
    """
    def __sub__(self, other):
        h = self.hours - other.hours
        m = self.minutes - other.minutes
        s = self.seconds - other.seconds
        return MyTime(h, m, s)

    """
    # Умножение.
    также но умножение
    """
    def __mul__(self, other):
        h = self.hours * other.hours
        m = self.minutes * other.minutes
        s = self.seconds * other.seconds
        return MyTime(h, m, s)

    """
    # Деление, оператор /.
    также, но деление и округление вниз по логике int(float)
    """
    def __truediv__(self, other):
        h = int(self.hours / other.hours)
        m = int(self.minutes / other.minutes)
        s = int(self.seconds / other.seconds)
        return MyTime(h, m, s)


time_0 = MyTime('12:45:58')  # строка + корректное время
print(time_0)
# time_0error = MyTime('12:45')  # строка + ValueError
time_1 = MyTime('25:61:61')  # строка + каждая часть больше нормы
print(time_1)
time_3 = MyTime()  # значения по умолчанию
print(time_3)
time_4 = MyTime(time_1)  # подаем класс на вход
print(time_4)
# time_5 = MyTime(123)  # ValueError
# time_6 = MyTime(1, 1, 12, 12)  # ValueError (кол-во входных параметров)

time_7 = MyTime('12:45:58')
time_8 = MyTime('13:45:58')
print(time_7 == time_8)  # >> False, because different hours
time_9 = MyTime('12:59:58')
print(time_9 == time_7)  # >> True, because equal hours
print(time_7 != time_8)  # >> True, because different hours
print(time_9 != time_7)  # >> False, because equal hours
print(time_9 < time_7)  # >> False, because equal hours
print(time_7 < time_8)  # >> True, because 7 < 8
print(time_9 > time_7)  # >> False, because equal hours
print(time_8 > time_7)  # >> True, because 8 > 7
print(time_9 <= time_7)  # >> True, because equal hours
print(time_7 <= time_8)  # >> True, because 7 < 8
print(time_8 <= time_7)  # >> False, because 7 < 8
print(time_9 >= time_7)  # >> True, because equal hours
print(time_8 >= time_7)  # >> True, because 8 > 7
print(time_7 >= time_8)  # >> False, because 8 > 7
time_10 = MyTime('3:33:33')
time_11 = MyTime('2:22:22')
print(time_10 + time_11)
print(time_10 - time_11)
print(time_10 * time_11)
print(time_10 / time_11)

"""
3. Разработать класс SuperStr, который наследует
функциональность стандартного типа str и содержит два
новых метода:
- метод is_repeatance(s), который принимает некоторую
строку и возвращает True или False в зависимости от того,
может ли текущая строка быть получена целым
количеством повторов строки s. Считать, что пустая
строка не содержит повторов
- метод is_palindrom(), который возвращает True или False в
зависимости от того, является ли строка палиндромом вне
зависимости от регистра. Пустую строку считать
палиндромом.
"""


class SuperStr(str):

    def is_repeatance(self, s):
        if not self and not s:
            return False
        else:
            count_of_repeats = len(str(self)) / len(s)
            if self == s * int(count_of_repeats):
                return True
            else:
                return False

    def is_palindrom(self):
        if self.lower() == self[::-1].lower():
            return True
        else:
            return False


text = SuperStr.is_palindrom('asdsa')
print(text)  # палиндром >> True
text = SuperStr.is_palindrom('asds')
print(text)  # не палиндром >> False
text = ''
print(SuperStr.is_repeatance(text, ''))  # пустая строка >> False
text = 'ab'
print(SuperStr.is_repeatance(text, 'abc'))  # >> False
text = 'abab'
print(SuperStr.is_repeatance(text, 'ab'))  # >> True
text = 'aba'
print(SuperStr.is_repeatance(text, 'abc'))  # >> False
text = 'aba'
print(SuperStr.is_repeatance(text, 'aba'))  # >> True
