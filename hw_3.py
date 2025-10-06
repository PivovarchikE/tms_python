# Задание 1
num_1, num_2, num_3 = int(input()), int(input()), int(input())
print(num_1 + num_2 + num_3)
print(num_1 - num_2 - num_3)
print(num_1 * num_2 * num_3)
print(num_1 - num_2 + num_3)
print(num_1 * num_2 / num_3)
print((num_1 + num_2) % num_3)

# Задание 2
from math import sqrt
cat_a, cat_b = float(input()), float(input())
area = cat_a * cat_b / 2
hypotenuse = sqrt(cat_a ** 2 + cat_b ** 2)
print(area, hypotenuse)

# Задание 3
text = [i for i in input().split()]
print(len(text))

# Задание 4
text = input()
ind_h_first = text.find('h')
ind_h_last = text.rfind('h')
text_1 = text[0:ind_h_first + 1:]
text_2 = text[ind_h_first + 1:ind_h_last:].replace('h', 'H')
text_3 = text[ind_h_last::]
text_out = text_1 + text_2 + text_3
print(text_out)

# Задание 5
text = input()
print(text[2])
print(text[-2])
print(text[0:5])
print(text[0:-2])
print(text[0::2])
print(text[1::2])
print(text[-1::-1])
print(text[-1::-2])
print(len(text))

# Задание 6
num = int(input())
print(num % 10)

# Задание 7
num = int(input())
tens = num // 10 % 10
print(tens)

# Задание 8
num = int(input())
sum_digits = 0
while num != 0:
    sum_digits += num % 10
    num = num // 10
print(sum_digits)