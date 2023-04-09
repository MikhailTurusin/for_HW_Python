# Задача 8:
# Требуется определить,
# 1. можно ли от шоколадки размером n × m долек отломить k долек,
# 2. если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# 3 2 4 -> yes
# 3 2 1 -> no

number1 = int(input("Введите длину шоколадки n: "))
number2 = int(input("Введите ширину шоколадки m: "))

number1_2 = number1 * number2
print(f"Размер шоколадки {number1*number2} долек")

number3 = int(input("Сколько долек k Вы хотите отломить от шоколадки: "))
if number3 < 1 or number3 > number1*number2-1:
    print("Некорректный ввод")
else:
    if number1_2 % 2 == 0:
        if number3 % 2 != 0:
            print(f"Нельзя отломать {number3} долек -> NO")
        else:
            print(f"Можно отломать {number3} долек -> YES")
    else:
        if number3 % 3 != 0:
            print(f"Нельзя отломать {number3} долек -> NO")
        else:
            print(f"Можно отломать {number3} долек -> YES")