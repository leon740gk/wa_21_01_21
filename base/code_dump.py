# Реализуйте серию из n игр "Камень, ножницы, бумага" с компьютером.
# В результате выведите статистику: сколько игр выиграл пользователь,
# сколько раз каждого вида ходов было выбрано.
# Дополните игру анализом компьютера ваших ходов и выбор наиболее подходящего против вас хода.

import random

games_number = int(input("How many games should we play? --> "))
print(f"Ok, you have {games_number} tries to beat me :)")
print("Rules: before each game please input on of:")
print("0 - Rock;")
print("1 - Paper;")
print("2 - Scissors;")
print("For exit game please input: 9")
print("Ready? Let's start!")

user_wins = 0
rock_chosen = 0
paper_chosen = 0
scissors_chosen = 0
user_choice = 0

while user_choice != 9 and games_number != 0:
    """
    Here put hte logic for simple ML
    """
    user_choice = int(input("Your turn: "))
    computer_choice = random.randint(0, 2)
    if user_choice == 0:
        rock_chosen += 1
        if computer_choice == user_choice or computer_choice == 1:
            pass
        else:
            user_wins += 1
        games_number -= 1

    elif user_choice == 1:
        paper_chosen += 1
        if computer_choice == user_choice or computer_choice == 2:
            pass
        else:
            user_wins += 1
        games_number -= 1

    elif user_choice == 2:
        scissors_chosen += 1
        if computer_choice == user_choice or computer_choice == 0:
            pass
        else:
            user_wins += 1
        games_number -= 1

    elif user_choice == 9:
        print("It's pity you wanna quit")
        break

    else:
        print("please, input valid number (0, 1, 2)")

print(f"User won {user_wins} times")
print(f"Rock choices: {rock_chosen} times")
print(f"Paper choices: {paper_chosen} times")
print(f"Scissors choices: {scissors_chosen} times")




# Пользователь вводит положительное целое число. Зашифровать каждую цифру серией из букв
# (конкретный принцип составления серии букв разработать самостоятельно).

user_input = input("Input number for encode: ")
code_chars = ""
for digit in user_input:
    for x in str(ord(digit)):
        code_chars += chr(int(x) + 65)

print(code_chars)

"""
Create decode implementation
"""




# В строке текста записаны слова, разделенные пробелами в произвольном количестве.
# Сжатие текста состоит в том, что между словами остается по одному пробелу,
# а после последнего слова пробелы удаляются (пробелы перед первым словом сохраняются).
# Если строка содержит только пробелы, то все они сохраняются.


def zipper(test_string):
    result_string = ""
    flag_1 = False
    flag_2 = False
    for i in test_string:
        if i == " " and not flag_1:
            result_string += i
        elif i == " " and flag_1 and not flag_2:
            flag_2 = True
            result_string += i
        elif i != " ":
            flag_1 = True
            flag_2 = False
            result_string += i

    return result_string.rstrip()

if __name__ == '__main__':
    test_str_1 = "  Hello world   this is   me   "
    test_str_2 = "Hello world   this is   me again   "
    test_str_3 = "      "
    test_str_4 = "   Hello world   this is  not actually me   :)"

    print(zipper(test_str_1))
    print(zipper(test_str_2))
    print(zipper(test_str_3))
    print(zipper(test_str_4))



# Сгенерировать пароль для пользователя.
# Требования: длина от 6 до 20 символов, должен быть ровно один символ подчеркивания,
# хотя бы две заглавных буквы, не более 5 цифр, любые две цифры подряд недопустимы.
import random

numbers = lambda: chr(random.randint(48, 57))
upper_letters = lambda: chr(random.randint(65, 90))
lower_letters = lambda: chr(random.randint(97, 122))
underscore = lambda: chr(95)
pass_generator = [numbers, upper_letters, lower_letters, underscore]
choose_pick = [0, 2, 3, 1, 0, 1, 2, 2, 2, 0, 2, 0, 1, 0, 2, 2, 1, 1, 1, 2]

password = ""
for i in range(random.randint(6, 20) + 1):
    password += pass_generator[choose_pick[i]]()

print(password)