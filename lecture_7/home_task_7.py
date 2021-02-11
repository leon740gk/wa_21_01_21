# завершить эту задачу согласно ТЗ и задекорировать функцию pass_generator так,
# что бы была возможность отследить колличество вызовов этой функции
# и сколько раз какой длянны был сгенерирован пароль
# (используйте замыкание во wrapper декоратора и словарь).

# ТЗ: Сгенерировать пароль для пользователя.
# Требования: длина от 6 до 20 символов, должен быть ровно один символ подчеркивания,
# хотя бы две заглавных буквы, не более 5 цифр, любые две цифры подряд недопустимы.

import random

def pass_generator():
    lower_letters = lambda: chr(random.randint(97, 122))
    upper_letters = lambda: chr(random.randint(65, 90))
    numbers = lambda: chr(random.randint(48, 57))
    underscore = lambda: chr(95)
    list_of_values = [lower_letters, upper_letters, numbers, underscore]
    choose_flow = [3, 1, 0, 0, 0, 2, 1, 2, 0, 0, 0, 2, 0, 2, 1, 0, 0, 0, 1, 2]

    password = ""
    for i in range(random.randint(6, 20)):
        symbol = list_of_values[choose_flow[i]]
        password += symbol()

    return password