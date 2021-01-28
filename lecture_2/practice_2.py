# Basic operations -----------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Пользователь вводит два числа. Найдите сумму и произведение данных чисел.
first_number = int(input("input first number: "))
second_number = int(input("input second number: "))

print(f"This is sum of numbers: {first_number + second_number}")
print(f"This is multiplication of numbers: {first_number * second_number}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Пользователь вводит число. Выведите на экран квадрат этого числа, куб этого числа.
number = int(input("input first number: "))
print(f"this num in square: {number ** 2}")
print(f"this num in power of three: {number ** 3}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Даны две переменных с некоторыми значениями. Поменять местами значения этих переменных
a = 7
b = 10
a, b = b, a
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Пользователь вводит три числа.
# Увеличьте первое число в два раза, второе число уменьшите на 3,
# третье число возведите в квадрат и затем найдите сумму новых трех чисел.
first_number = int(input("input first number: "))
second_number = int(input("input second number: "))
third_number = int(input("input third number: "))

new_f_num = first_number * 2
new_s_num = second_number - 3
new_t_num = third_number ** 2

print(f"Result: {new_f_num + new_s_num + new_t_num}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Пользователь вводит три числа.
# Найдите среднее арифметическое этих чисел,
# а также разность (удвоенной (суммы первого и третьего чисел)) и (утроенного второго числа).
first_number = int(input("input first number: "))
second_number = int(input("input second number: "))
third_number = int(input("input third number: "))

avg_nums = (first_number + second_number + third_number) / 3
double_sum_of_1_3 = (first_number + third_number) * 2
triple_2 = second_number * 3
diff = double_sum_of_1_3 - triple_2

print(f"{avg_nums}")
print(f"{diff}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Conditions -----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Дано число. Если оно больше 3, то увеличить число на 10, иначе уменьшить на 10.
number = int(input("input number: "))

if number > 3:
    print(f"result: {number + 10}")
else:
    print(f"result: {number - 10}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Пользователь вводит номер месяца, вывести название месяца.
number_of_month = int(input("Please enter number between 1 - 12: "))

if number_of_month == 1:
    print("January")
elif number_of_month == 2:
    print("February")
elif number_of_month == 3:
    print("March")
elif number_of_month == 4:
    print("April")
elif number_of_month == 5:
    print("May")
else:
    print("Please enter number between 1 - 12")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Дано два числа. Вывести наибольшее из них.
num_1 = int(input("input first num: "))
num_2 = int(input("input second num: "))

print(f"Max number is: {max(num_1, num_2)}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



# Loops  ---------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Пользователь вводит ненулевые целые числа до тех пор, пока не введет ноль.
# Найдите количество четных чисел, которые он ввел.
#
num = None
count = 0
while num != 0:
    num = int(input("please input number. if you want to exit, input 0: "))
    if num == 0:
        break
    if num % 2 == 0:
        print("Even")
        count += 1

print(f"Result: {count}")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
