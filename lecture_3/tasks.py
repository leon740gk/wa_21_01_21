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
