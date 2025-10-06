import os
import json
import csv
import sys


"""
1.
# Код работает только, если ранее в данном каталоге подобная сортировка не
проводилась. Можно доработать, но надо время)
"""


def sorting_files():
    print(f'Имя системы: {os.name}')
    print(f'Текущий каталог: {os.getcwd()}')
    """
    Cоздаём словарь, в котором будем накапливать имена созданных каталогов,
    их количество и размер
    """
    sorting_result = {}
    for i in os.listdir():

        if os.path.isfile(i):
            """
            проверяем, что текущий обрабатываемый файл не является файлом с нашей
            программой (исполняемым файлом)
            """
            if i != os.path.basename(__file__):
                name, extension = os.path.splitext(i)
                """
                проверяем наличие расширения, если у файла нет расширения, то создадим
                под это дело каталог
                """
                if extension:
                    name_of_directory = extension[1:]
                else:
                    name_of_directory = 'no_extension'

                if not os.path.exists(name_of_directory):
                    os.mkdir(name_of_directory)
                    sorting_result[name_of_directory] = [0, 0]
                    sorting_result[name_of_directory][0] += 1
                    sorting_result[name_of_directory][1] += os.path.getsize(i)
                    os.replace(i, os.path.join(name_of_directory, i))

                else:
                    sorting_result[name_of_directory][0] += 1
                    sorting_result[name_of_directory][1] += os.path.getsize(i)
                    os.replace(i, os.path.join(name_of_directory, i))

    # no comment)
    for key, val in sorting_result.items():
        print(f'В папку с файлами "{key}" перемещено файлов - {val[0]}, их суммарный размер - {val[1]} байт')

    # получаем список объектов, проверяем являются ли они папками, заходим в первую папку, переименовываем первый файл
    for i in os.listdir():
        if os.path.isdir(i):
            for k in os.listdir(i):
                cur_path = os.path.join(os.getcwd(), i)
                os.replace(os.path.join(cur_path, k), os.path.join(cur_path, 'renamed_file'))
                print(f'Файл "{k}" переименован в "renamed_file"')
                break
            break
        break


sorting_files()

# 2.
with open("1.txt", 'r', encoding='UTF8') as data_set:
    file_lines = data_set.readlines()
print(file_lines[0].strip())
print(file_lines[4].strip())
print(*file_lines[0:4], end='', sep='')
s1, s2 = (int(input('Введите первую строку диапазона\n')),
          int(input('Введите вторую строку диапазона\n')))
print(*file_lines[s1:s2 + 1], end='', sep='')
print(*file_lines, end='', sep='')

# 3.
with open('file_for_input_from_stdin', 'w', encoding='UTF8') as file:
    for _ in range(6):
        file.write(input('Введите текст, который надо добавить в файл\n') + '\n')


# 4.
with open('file_for_input_from_stdin', 'r', encoding='UTF8') as file_1:
    stop = False
    for ind_1, str_1 in enumerate(file_1, start=1):
        with open("1.txt", 'r', encoding='UTF8') as file_2:
            for ind_2, str_2 in enumerate(file_2, start=1):
                if ind_1 == ind_2:
                    if str_1.strip() != str_2.strip():
                        print(ind_1)
                        stop = True
                        break
                    else:
                        break
        if stop:
            break
    else:
        if not stop:
            print('Все строки совпадают')


'''
5.
Я бы ещё много чего дописал в программе ниже,
но времени уже физически не хватает )
'''


def employees_data():

    def start():
        functions = {
            1: 'Считать данные работников из JSON и преобразовать их в CSV',
            2: 'Сохранить данные работников из JSON в CSV-файл',
            3: 'Добавить данные работника в JSON-файл',
            4: 'Добавить данные работника в CSV-файл',
            5: 'Поиск данных о работнике по имени',
            6: 'Фильтр работников по языку программирования',
            7: 'Вывести средний рост всех сотрудников, у которых год '
               'рождения меньше заданного',
            8: 'Выход'}

        print('Выберите действие (введите цифру):')
        for key, val in functions.items():
            print(f'{key} - {val}')

    def json_convert_to_csv():
        with open('employees.json', 'r', encoding='UTF8') as emp:
            data = json.load(emp)
            data_in_csv = ''
            data_in_csv = data_in_csv + ';'.join(data[0].keys()) + '\n'
            for i in data:
                for value in i.values():
                    if type(value) != list:
                        data_in_csv += str(value) + ';'
                    else:
                        data_in_csv += ','.join(value)
                data_in_csv += '\n'
        return data_in_csv


    def json_to_csv_save():
        name_of_saving_csv_file = input('Введите имя CSV-файла\n')
        with open(name_of_saving_csv_file + '.csv', 'w',
                  encoding='UTF8') as w_file:
            w_file.write(json_convert_to_csv())
        return None

    def add_new_employee_to_json():
        print('Введите данные работника:\n')
        name = input('Имя:\n')
        birthday = input('Дата рождения в формате дд.мм.гггг:\n')
        height = float(input('Рост в см.:\n'))
        weight = float(input('Вес в кг.:\n'))
        car = input('Наличие авто (да/нет):\n')
        if car.lower() == 'да':
            car = True
        elif car.lower() == 'нет':
            car = False
        languages = input('Языки программирования через запятую\n').split(',')

        json_data = {
            "name": name,
            "birthday": birthday,
            "height": height,
            "weight": weight,
            "car": car,
            "languages": languages
        }

        with open('employees.json', 'r', encoding='UTF8') as j_file:
            data = json.load(j_file)

        data.append(json_data)

        with open('employees.json', 'w', encoding='UTF8') as j_file:
            json.dump(data, j_file, ensure_ascii=False, indent=4)

    def add_new_employee_to_csv():
        name_of_saving_csv_file = input(
            'Введите имя CSV-файла, в который надо добавить данные\n')
        print('Введите данные работника:')
        name = input('Имя:\n')
        birthday = input('Дата рождения в формате дд.мм.гггг:\n')
        height = input('Рост в см.:\n')
        weight = input('Вес в кг.:\n')
        car = input('Наличие авто (да/нет):\n')

        if car.lower() == 'да':
            car = True
        elif car.lower() == 'нет':
            car = False

        languages = input('Языки программирования через запятую\n')

        csv_data = name + ';' + birthday + ';' + height + ';' + weight + ';' + str(
            car) + ';' + ''.join(languages.split()) + '\n'

        with open(name_of_saving_csv_file, 'a', encoding='UTF8') as csv_file:
            csv_file.write(csv_data)

    def find_employee_in_csv_by_name():
        filename = input(
            'Введите имя CSV-файла, в котором будем искать работника\n')
        name_of_employee = input('Введите имя работника\n')

        with open(filename, 'r', encoding='UTF8') as csv_file:
            filereader = csv.reader(csv_file, delimiter=';')
            flag = False
            for row in filereader:
                if row[0] == name_of_employee:
                    print(f'Имя - {row[0]}\n'
                          f'Дата рождения - {row[1]}\n'
                          f'Рост - {row[2]}\n'
                          f'Вес - {row[3]}\n'
                          f'Наличие авто - {row[4]}\n'
                          f'Языки программирования - {row[5]}\n')
                    flag = True
            if not flag:
                print('Работник в БД не найден\n')

    def find_employee_in_csv_by_language():
        filename = input(
            'Введите имя CSV-файла, в котором будем искать работника\n')
        language = input('Введите язык\n')

        with open(filename, 'r', encoding='UTF8') as csv_file:
            filereader = csv.reader(csv_file, delimiter=';')
            employees_list = []

            for row in filereader:
                for ind, val in enumerate(row[5].split(',')):
                    if language == val:
                        employees_list.append(row[0])

            result = employees_list if employees_list else None
            return result

    def avg_height_employee_in_csv_by_birth_year():
        filename = input(
            'Введите имя CSV-файла, в котором будем искать работника\n')
        year_birth = input('Введите год рождения\n')

        avg_height = 0

        with open(filename, 'r', encoding='UTF8') as csv_file:
            filereader = csv.reader(csv_file, delimiter=';')
            sum_heights = 0
            count = 0

            for row in filereader:
                for ind, val in enumerate(row[1].split('.')):
                    if ind == 2 and (val < year_birth):
                        sum_heights += float(row[2])
                        count += 1
        if count > 0:
            avg_height = round(sum_heights / count, 2)

        result = avg_height if avg_height else None
        return result


    while True:
        start()
        action = int(input())

        if action == 1:
            print('-------------------------------')
            json_convert_to_csv()
            print(json_convert_to_csv())
            print(f'Данные успешно конвертированы\n'
                  f'-------------------------------\n')

        elif action == 2:
            print('-------------------------------')
            json_to_csv_save()
            print(f'Данные успешно сохранены\n'
                  f'-------------------------------\n')


        elif action == 3:
            print('-------------------------------')
            add_new_employee_to_json()
            print(f'Данные успешно добавлены\n'
                  f'-------------------------------\n')

        elif action == 4:
            print('-------------------------------')
            add_new_employee_to_csv()
            print(f'Данные успешно добавлены\n'
                  f'-------------------------------\n')
        elif action == 5:
            print('-------------------------------')
            find_employee_in_csv_by_name()
            print('-------------------------------\n')
        elif action == 6:
            print('-------------------------------')
            print(find_employee_in_csv_by_language())
            print('-------------------------------\n')
        elif action == 7:
            print('-------------------------------')
            print(avg_height_employee_in_csv_by_birth_year())
            print('-------------------------------\n')

        elif action == 8:
            print('Спасибо за использование нашего сервиса')
            sys.exit()

employees_data()
