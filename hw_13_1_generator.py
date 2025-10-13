"""
Реализовать программу для бесконечной циклической
последовательности чисел (например, 1-2-3-1-2-3-1-2...).
Последовательность реализовать с помощью генераторной
функции, количество чисел для вывода задаётся
пользователем с клавиатуры.
"""


def my_gen(nums) -> int:
    while True:
        for i in nums:
            yield i


a = my_gen(start_in, end_in, step_in)

try:
    for i in a:
        if i < 20:
            print(i)
        else:
            break
except ValueError as err:
    print(err)
