from random import randint

# 1.
list_of_numbers = [-1, 1, 2, 3, 7, 9, 12, 22, 25, 33]
num_for_search = -1


def binary_search(input_data_list, num):
    index_num_in_the_middle = len(input_data_list) // 2

    if num == input_data_list[index_num_in_the_middle]:
        return index_num_in_the_middle
    elif num < input_data_list[index_num_in_the_middle]:
        return binary_search(input_data_list[0:index_num_in_the_middle], num)
    else:
        return (binary_search(input_data_list[index_num_in_the_middle + 1:], num)
                + index_num_in_the_middle + 1)


print(f"Индекс искомого элемента = {binary_search(list_of_numbers, num_for_search)}")


# 2.
n = int(input('Введите целое число\n'))

def to_binary(num):
    binary_num_list = []
    num_temp = abs(num)
    while num_temp != 0:
        binary_num_list.append(num_temp % 2)
        num_temp = num_temp // 2
    if num >= 0:
        binary_num_list.insert(0, '0.')
    else:
        for ind, val in enumerate(binary_num_list):
            if val == 0:
                binary_num_list[ind] = 1
            elif val == 1:
                binary_num_list[ind] = 0
        binary_num_list.insert(0, '1.')

    return binary_num_list

print(*to_binary(n), sep='')

"""
3.
Мне не нравится это решение из-за кривости, но оно было быстрым )
num = int(input('Введите целое положительное число\n'))
"""

def is_prime_number(number):
    if number < 2:
        return False

    counter = 0
    for i in range(1, number + 1):
        if (number % i == 0) and (counter <= 2):
            counter += 1
        elif counter > 2:
            return False
    else:
        if counter > 2:
            return False
        else:
            return True


print(is_prime_number(num))


# 4.
num_1, num_2 = [abs(int(i)) for i in input('Введите 2 целых числа через пробел\n').split()]


def least_common_divisor(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return b


print(least_common_divisor(num_1, num_2))

# 5
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
rus_upper_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


# проверка на корректность ввода числа (выбор шифрование/дешифрование)
def is_valid(num_input):
    if num_input.isnumeric():
        if int(num_input) == 2 or int(num_input) == 1:
            return True
    else:
        return False


# проверка на корректность ввода числа (шаг сдвига)
def is_valid_step(num_input):
    if num_input.isnumeric():
        if int(num_input) >= 1:
            return True
    else:
        return False


# расшифровка текста
def to_encrypt(text_input, lang, step):
    encrypt_return = ''
    if int(lang) == 1:
        for ind, val in enumerate(text_input):
            if val.isupper():
                encrypt_return += \
                    rus_upper_alphabet[(rus_upper_alphabet.find(val) + int(step)) % len(rus_upper_alphabet)]
            elif val.islower():
                encrypt_return += \
                    rus_lower_alphabet[(rus_lower_alphabet.find(val) + int(step)) % len(rus_lower_alphabet)]
            else:
                encrypt_return += val
    elif int(lang) == 2:
        for ind, val in enumerate(text_input):
            if val.isupper():
                encrypt_return += \
                    eng_upper_alphabet[(eng_upper_alphabet.find(val) + int(step)) % len(eng_upper_alphabet)]
            elif val.islower():
                encrypt_return += \
                    eng_lower_alphabet[(eng_lower_alphabet.find(val) + int(step)) % len(eng_lower_alphabet)]
            else:
                encrypt_return += val
    return encrypt_return


# шифровка текста
def to_decrypt(text_input, lang, step):
    decrypt_return = ''
    if int(lang) == 1:
        for ind, val in enumerate(text_input):
            if val.isupper():
                decrypt_return += \
                    rus_upper_alphabet[(rus_upper_alphabet.find(val) - int(step)) % len(rus_upper_alphabet)]
            elif val.islower():
                decrypt_return += \
                    rus_lower_alphabet[(rus_lower_alphabet.find(val) - int(step)) % len(rus_lower_alphabet)]
            else:
                decrypt_return += val
    elif int(lang) == 2:
        for ind, val in enumerate(text_input):
            if val.isupper():
                decrypt_return += \
                    eng_upper_alphabet[(eng_upper_alphabet.find(val) - int(step)) % len(eng_upper_alphabet)]
            elif val.islower():
                decrypt_return += \
                    eng_lower_alphabet[(eng_lower_alphabet.find(val) - int(step)) % len(eng_lower_alphabet)]
            else:
                decrypt_return += val
    return decrypt_return


# проверка на символы другого языка
def is_language_valid(text_input, lang):
    flag_lang = True
    if int(lang) == 1:
        for ind, val in enumerate(text_input):
            if val.islower():
                if val not in rus_lower_alphabet:
                    flag_lang = False
                    break
            elif val.isupper():
                if val not in rus_upper_alphabet:
                    flag_lang = False
                    break
    elif int(lang) == 2:
        for ind, val in enumerate(text_input):
            if val.islower():
                if val not in eng_lower_alphabet:
                    flag_lang = False
                    break
            elif val.isupper():
                if val not in eng_upper_alphabet:
                    flag_lang = False
                    break
    return flag_lang


print('Привет. Что будем делать? Введи 1 - если шифруем, 2 - если дешифруем:')
while True:
    what_do_answer = input()
    if not is_valid(what_do_answer):
        print('Был введён некорректный ответ. Введи 1 - если шифруем, 2 - если дешифруем:')
        continue
    else:
        break


print('С каким языком будем работать? Введи 1 - если с русским, 2 - если с английским:')
while True:
    what_language = input()
    if not is_valid(what_language):
        print('Был введён некорректный ответ. Введи 1 - если будем работать с русским языком, 2 - если с английским:')
        continue
    else:
        break

print('Введи шаг сдвига шифрования вправо (целое число больше 0):')
while True:
    step_shift = input()
    if not is_valid_step(step_shift):
        print('Был введён некорректный ответ. Введи целое число больше 0:')
        continue
    else:
        break


if int(what_do_answer) == 1:
    print('Введите текст для шифрования:')
    while True:
        text = input()
        if not is_language_valid(text, what_language):
            print('В тексте содержатся символы иного алфавита. Введи текст, состоящий из символов русского алфавита:')
            continue
        else:
            break
    print(to_encrypt(text, what_language, step_shift))
elif int(what_do_answer) == 2:
    print('Ввведите текст для дешифрования:')
    while True:
        text = input()
        if not is_language_valid(text, what_language):
            print('В тексте содержатся символы иного алфавита. '
                  'Введи текст, состоящий из символов английского алфавита:')
            continue
        else:
            break
    print(to_decrypt(text, what_language, step_shift))


# 6*.1 Шифровка на примере строчных английских символов
data_to_encrypt = 'ATTACKATDAWN'
code_word = 'LEMON'

eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def to_encrypt(text_input, step):
    encrypt_return = ''
    for ind, val in enumerate(text_input):
        encrypt_return += \
            eng_upper_alphabet[
                (eng_upper_alphabet.find(val) + int(step)) % len(
                    eng_upper_alphabet)]

    return encrypt_return

def encrypt_viginere(word_to_encrypt, code):
    word_to_shift = ''
    ind = 0
    while len(word_to_shift) != len(word_to_encrypt):
        if ind != len(code):
            word_to_shift += code[ind]
            ind += 1
        else:
            ind = 0

    encrypted_word = ''

    for i in range(len(word_to_encrypt)):
        symb_enc, symb_cod = word_to_encrypt[i], word_to_shift[i]
        encrypted_word += to_encrypt(symb_enc, eng_upper_alphabet.index(symb_cod))

    return encrypted_word


print(encrypt_viginere(data_to_encrypt, code_word))
print('LXFOPVEFRNHR - проверочное слово ')

# 6.2 Дешифровка на примере строчных английских символов

data_to_decrypt = 'LXFOPVEFRNHR'
code_word = 'LEMON'

eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def to_decrypt(text_input, step):
    encrypt_return = ''
    for ind, val in enumerate(text_input):
        encrypt_return += \
            eng_upper_alphabet[(eng_upper_alphabet.find(val) - int(step)) % len(eng_upper_alphabet)]
    return encrypt_return

def decrypt_viginere(word_to_decrypt, code):
    word_to_shift = ''
    ind = 0
    while len(word_to_shift) != len(word_to_decrypt):
        if ind != len(code):
            word_to_shift += code[ind]
            ind += 1
        else:
            ind = 0

    decrypted_word = ''

    for i in range(len(word_to_decrypt)):
        symb_enc, symb_cod = word_to_decrypt[i], word_to_shift[i]
        decrypted_word += to_decrypt(symb_enc, eng_upper_alphabet.index(symb_cod))

    return decrypted_word


print(decrypt_viginere(data_to_decrypt, code_word))
print('ATTACKATDAWN - проверочное слово')


'''
7.
Для всех следующих задач кроме 14-ой можно оставить эту uncommented
и будет готовая матрица по заданным через пробел M и N
'''

m, n = [int(i) for i in input().split()]


def create_matrix(len_rows, len_columns):
    mat = []
    for _ in range(len_rows):
        row = []
        for _ in range(len_columns):
            row.append(randint(0, 9))
        mat.append(row)
    return mat

matrix = create_matrix(m, n)
for row in matrix:
    print(*row)

# 8.
def find_min_max_in_matrix(mat):
    max_coordinates = []
    min_coordinates = []
    max_num = matrix[0][0]
    min_num = matrix[0][0]

    for i in mat:
        temp = max(i)
        if temp > max_num:
            max_num = temp

    for i in mat:
        temp = min(i)
        if temp < min_num:
            min_num = temp

    flag = False

    for row in range(m):
            for column in range(n):
                if mat[row][column] == max_num:
                    max_coordinates = [row,column]
                    flag = True
                    break
            if flag:
                break

    flag = False

    for row in range(m):
            for column in range(n):
                if mat[row][column] == min_num:
                    min_coordinates = [row,column]
                    flag = True
                    break
            if flag:
                break

    return max_coordinates, min_coordinates

print(find_min_max_in_matrix(matrix))

# 9.

def sum_all_elements_of_matrix(mat):
    sum_elements = 0
    sum_columns = [0 for i in range(len(mat[0]))]
    for row in range(m):
        for column in range(n):
            sum_elements += mat[row][column]
            sum_columns[column] += mat[row][column]
    return sum_elements, sum_columns

elements_sum, columns_sum = sum_all_elements_of_matrix(matrix)
proportions = []
for ind, val in enumerate(columns_sum):
    print(f"Доля суммы элементов столбца {ind + 1} в общей сумме элементов матрицы =  {round((val / elements_sum * 100), 2)}%")

print(f"Сумма всех элементов = {elements_sum}")

# 10*.
number_or_column_to_sum = int(input('Введите индекс столбца, который будем прибавлять\n'))

def column_multiply_column(mat, num):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = mat[i][j] * mat[i][num]
    return mat


for row in column_multiply_column(matrix, number_or_column_to_sum):
    print(*row)


'''
11*. 
Вопрос: Постоянная проблема, что я вне функции получаю переменную и потом надо
использовать её внутри функции. Хочется называть одинаково, но это
неправильно. Как здесь лучше поступить? В функции называть как-то 
упрощённо (m, n, num, и т.д.) и описывать суть в строке документации?
'''
number_or_row_to_sum = int(input('Введите индекс строки, которую будем прибавлять\n'))

def row_plus_row(mat, num):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = mat[i][j] + mat[num][j]
    return mat


for row in row_plus_row(matrix, number_or_row_to_sum):
    print(*row)


"""
12.
я тестировал с активным кодом из 7 задачи, поэтому в функции 
использую m и n. # Но если писать отдельно, то логичней было бы 
использовать len от матрицы и от нулевого элемента матрицы
"""

H = int(input('Введите число, которое надо найти\n'))

def find_in_matrix(mat, num_for_find):
    dict_of_counter = {i: 0 for i in range(len(mat[0]))}
    for row in range(m):
        flag = False
        for column in range(n):
            if mat[row][column] == num_for_find:
                dict_of_counter[column] = dict_of_counter[column] + 1
                break


    return dict_of_counter
result = find_in_matrix(matrix, H)
print(result)

# 13. 
def sum_elements_diagonals(mat):
    count_of_rows = len(mat)
    sum_elements_main_diagonal = 0
    for i in range(count_of_rows):
        sum_elements_main_diagonal += mat[i][i]

    sum_elements_secondary_diagonal = 0

# ниже минусуем count_or_rows, чтобы двигаться вниз по побочной диагонали
    for k in range(count_of_rows):
        sum_elements_secondary_diagonal += matrix[k][count_of_rows - 1]
        count_of_rows -= 1

    return sum_elements_main_diagonal, sum_elements_secondary_diagonal


main_diagonal,  secondary_diagonal = sum_elements_diagonals(matrix)
print(f"Сумма элементов главной диагонали = {main_diagonal}\n"
      f"Сумма элементов побочной диагонали = {secondary_diagonal}")


14.
m, n = [int(i) for i in input().split()]


def create_matrix(len_rows, len_columns):
    mat = []
    for _ in range(len_rows):
        row = []
        for _ in range(len_columns):
            row.append(randint(0, 1))
        mat.append(row)
    return mat

matrix = create_matrix(m, n)
for row in matrix:
    print(*row)

def make_number_digits_one_even(mat):
    counter = 0
    for row in mat:
        for ind, val in enumerate(row):
            if ind != (len(row) - 1):
                if val == 1:
                    counter += 1
            else:
                if val == 1:
                    counter += 1
                if counter % 2 != 0:
                    row.append(1)
                    counter = 0
                    break
                else:
                    row.append(0)
                    counter = 0
                    break
    return mat

result = make_number_digits_one_even(matrix)
for row in result:
    print(*row)
