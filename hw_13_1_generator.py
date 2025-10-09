"""
Реализовать программу для бесконечной циклической
последовательности чисел (например, 1-2-3-1-2-3-1-2...).
Последовательность реализовать с помощью генераторной
функции, количество чисел для вывода задаётся
пользователем с клавиатуры.
"""


def my_gen(start: int, end: int, step: int) -> int:
    if step <= 0:
        raise ValueError('Step could be > 0')

    temp = start

    if end >= start:
        while True:
            if temp <= end:
                yield temp
                temp += step
            else:
                temp = start
    else:
        while True:
            if temp >= end:
                yield temp
                temp -= step
            else:
                temp = start
start_in, end_in, step_in = (int(input('Enter the initial value\n')),
                             int(input('Enter the final value\n')),
                             int(input('Enter the step value\n')))


a = my_gen(start_in, end_in, step_in)

try:
    for i in a:
        if i < 20:
            print(i)
        else:
            break
except ValueError as err:
    print(err)
