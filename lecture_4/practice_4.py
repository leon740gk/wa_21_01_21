# Lists --------------------------------------------------------------------------------
# Заполнить массив нулями, кроме первого и последнего элементов, которые должны быть равны единице.
# output_list = []
# n = 40
# for i in range(n):
#     if i == 0 or i == n-1:
#         output_list.append(1)
#     else:
#         output_list.append(0)
#
# print(output_list)

# Заполнить массив нулями и единицами, при этом данные значения чередуются, начиная с нуля.
# output_list = []
# n = 40
# for i in range(n):
#     if i % 2 == 0:
#         output_list.append(0)
#     else:
#         output_list.append(1)
#
# print(output_list)


# Заполнить массив последовательными нечетными числами, начиная с единицы.
# output_list = []
# n = 40
# for i in range(1, n):
#     if i % 2 != 0:
#         output_list.append(i)
#
# print(output_list)


# Поменять местами наибольший и наименьший элементы массива.

# a = [12, 2334, 454, 23, 3454, 44, 23245, 3, 2332]
# min = None
# index_min = 0
# max = None
# index_max = 0
# for index, value in enumerate(a):
#     if index == 0:
#         min = max = value
#         continue
#     if value < min:
#         min = value
#         index_min = index
#     if value > max:
#         max = value
#         index_max = index
#
# a[index_min], a[index_max] = a[index_max], a[index_min]
#
# print(f"{a}")


# Даны входные данные (номера страховых полисов клиентов двух больних (списки):
# Alchemilla Hospital и Brookhaven Hospital).
# Нужно выяснить:
# 1. Сколько клиентов посещают обе больницы
# 2. Сколько клиентов посещают только больницу Alchemilla Hospital
# 3. Сколько клиентов (уникальных страховых полисов) находится в базах данных всех больниц
# Input data: al_hospital = [123, 4325, 3567, 234, 54647, 5663]
# Input data: bh_hospital = [688, 5653, 123, 56778, 234, 4677, 8787]
# # To solve with and without sets
#
# al_hospital = [123, 4325, 3567, 234, 54647, 5663]
# bh_hospital = [688, 5653, 123, 56778, 234, 4677, 8787]

# check_list = []
# for i in al_hospital:
#     for j in bh_hospital:
#         if i == j:
#             check_list.append(i)
#
# print(check_list)


# Sets --------------------------------------------------------------------------------
# Даны массивы с произвольным набором данных (в каждом массиве только один тип данных)
# Убедиться, что в них нет повторяющихся элементов (любой подходящий способ)

# a = [23, 23 ,223, 23, 32, 3434 , 1, 1, 2, 3]
# print(list(set(a)))

# Даны входные данные (номера страховых полисов клиентов двух больних (списки):
# Alchemilla Hospital и Brookhaven Hospital).
# Нужно выяснить:
# 1. Сколько клиентов посещают обе больницы
# 1. Сколько клиентов посещают только больницу Alchemilla Hospital
# 1. Сколько клиентов (уникальных страховых полисов) находится в базах данных всех больниц
# Input data: al_hospital = [123, 4325, 3567, 234, 54647, 5663]
# Input data: bh_hospital = [688, 5653, 123, 56778, 234, 4677, 8787]
# To solve with and without sets

# al_hospital = [123, 4325, 3567, 234, 54647, 5663]
# bh_hospital = [688, 5653, 123, 56778, 234, 4677, 8787]
#
# al_set = set(al_hospital)
# bh_set = set(bh_hospital)
#
# print(al_set.intersection(bh_set))
# print(al_set.difference(bh_set))
#
# print(al_set.union(bh_set))



# Dictionaries ---------------------------------------------------------------------------

# Пользователь вводит номер месяца, вывести название месяца.
# (попробуйте решить с применением словаря)
#
# months_mapper = {
#     1: "January",
#     2: "February",
#     3: "March",
#     4: "April",
#     5: "May",
#     6: "June",
#     7: "July",
#     8: "Aug",
#     9: "Sep",
#     10: "Oct",
#     11: "Nov",
#     12: "Dec",
# }
#
# while True:
#     month_num = int(input("please enter month num. for exit enter 0: "))
#     if month_num == 0:
#         break
#     print(months_mapper[month_num])