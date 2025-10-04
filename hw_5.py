# Задание 2
price_of_phone = float(input('Маша, сколько рублей стоит твой телефон?\n'))
daily_amount = int(input('Сколько денег ты готова откладывать в день?\n'))
accumulated_amount = 0
day_of_week = 0

while accumulated_amount < price_of_phone:
    day_of_week += 1
    if day_of_week % 7 != 0:
        accumulated_amount += daily_amount

print(f'Маша, так ты накопишь на телефон за {day_of_week} дней.')


# Задание 3
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


input_data = int(input('Для расчет n-го числа Фибоначчи введите целое '
                       'неотрицательное число\n'))
print(f"Для числа {input_data} n-ое число Фибоначчи = {fib(input_data)}")

# Задание 4
list_input = [float(i) for i in input('Введите список чисел через пробел, '
                                      'целую часть от десятичной отделяйте '
                                      'точкой, минус не отделяйте пробелом '
                                      'от числа\n').split()]
sum_of_values = sum(list_input)
min_value = min(list_input)
max_value = max(list_input)

print(
      f'Сумма всех значений = {sum_of_values}\n'
      f'Минимальное значение = {min_value}\n'
      f'Максимальное значение = {max_value}'
      )

# Задание 5

list_input = [float(i) for i in input('Введите список чисел через пробел, '
                                      'целую часть от десятичной отделяйте '
                                      'точкой, минус не отделяйте пробелом '
                                      'от числа\n').split()]
dict_of_count = {}

if len(list_input) == len(set(list_input)):
    print('Все элементы списка уникальны')
else:
    for num in list_input:
        if num not in dict_of_count:
            dict_of_count[num] = 1
        else:
            dict_of_count[num] = dict_of_count.get(num, 0) + 1
    for key, value in dict_of_count.items():
        if value > 1:
            print(f'Вот список пар "число - количество повторений" для '
                  f'дубликатов: {key} - {value}')
