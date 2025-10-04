# 1.
def body_mass_index():
    print(f'Калькулятор индекса массы тела приветствует вас')

    while True:
        try:
            height = float(input('Введите рост в сантиметрах\n'))

            if height <= 0:
                print('Такой рост невозможен')
                break

            weight = float(input('Введите вес в килограммах\n'))

            if weight < 0:
                print('Такой вес невозможен')
                break

        except KeyboardInterrupt:
            print(f'Возникла предвиденная ошибка - KeyboardInterrupt')
            break
        except ValueError as e:
            print(f'Возникла предвиденная ошибка - ValueError ({e}).')
            break

        try:
            bmi = round(weight / (height / 100) ** 2, 2)

            if bmi <= 16:
                print(f'ИМТ: {bmi} - выраженный дефицит массы тела')
                break
            elif 16 <= bmi < 18.5:
                print(f'ИМТ: {bmi} - недостаточная(дефицит) масса тела')
                break
            elif 18.5 <= bmi < 25:
                print(f'ИМТ: {bmi} - норма')
                break
            elif 25 <= bmi < 30:
                print(f'ИМТ: {bmi} - избыточная масса тела (предожирение)')
                break
            elif 30 <= bmi < 35:
                print(f'ИМТ: {bmi} - ожирение первой степени')
                break
            elif 35 <= bmi < 40:
                print(f'ИМТ: {bmi} - ожирение второй степени')
                break
            elif bmi >= 40:
                print(f'ИМТ: {bmi} - ожирение третьей степени (морбидное)')
                break
        except ZeroDivisionError as e:
            print(f'Возникла предвиденная ошибка - ZeroDivisionError ({e}). '
                  f'Говорят, что если попытаться разделить ненулевое число '
                  f'на ноль, произойдет математический абсурд.')
            break

body_mass_index()


# 2.
def my_calc():
    print(f'Калькулятор (игра сломай программу) приветствует вас!\n'
          f'- на вход принимаю число, операцию, число и выдаю ответ\n'
          f'- допустимые операции: +, -, *, /, **\n'
          f'- для выхода введите "exit".')
    try:
        while True:
            num_1 = input('Введите число 1\n')

            if num_1.lower() == 'exit':
                break

            operation = input('Введите операцию\n')

            if operation.lower() == 'exit':
                break

            num_2 = input('Введите число 2\n')

            if num_2.lower() == 'exit':
                break

            num_1 = float(num_1)
            num_2 = float(num_2)

            if operation == '+':
                print(f'Ответ: {num_1 + num_2}')
            elif operation == '-':
                print(f'Ответ: {num_1 - num_2}')
            elif operation == '*':
                print(f'Ответ: {num_1 * num_2}')
            elif operation == '/':
                print(f'Ответ: {num_1 / num_2}')
            elif operation == '**':
                print(f'Ответ: {num_1 ** num_2}')

            print('--------------------------')
    except KeyboardInterrupt:
        print(f'Возникла предвиденная ошибка - KeyboardInterrupt')
    except ZeroDivisionError as e:
        print(f'Возникла предвиденная ошибка - ZeroDivisionError ({e}). '
              f'Кто-то пытался делить на ноль.')
    except ValueError as e:
        print(f'Возникла предвиденная ошибка - ValueError ({e}).')

    return None
my_calc()
