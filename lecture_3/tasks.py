# Создать простейшую программу для пропускного контроля людей в зависимости от их возратса.
# Выводить соответствующие сообщения.

age = int(input("Please enter your age: "))

if age < 18:
    print("To little :)")
elif age < 25:
    print("You've got an discount 20%")
elif age <= 50:
    print("You are welcome !")
else:
    print("Go get some rest")


# Дан массив из строк. Определить максимально быстро и эффективно, есть ли в строках цифры.
# Если в строке есть цифра - вывести ее (строку) на экран (single time).
# Input: ["asd3yhy4", "34355fe", "sdfvsdfvsd", "   ", "567h65h", "aaaaaa"]

# Additional task: После того, как вы найдете первую цифру в строке,
# прекратить поиск цифр в этой строке.
# Перейти к поиску цифр в следующей строке.

input_data = ["asd3yhy4", "34355fe", "sdfvsdfvsd", "   ", "567h65h", "aaaaaa"]

for i in input_data:
    for j in i:
        if j.isdigit():
            print(i)
            break