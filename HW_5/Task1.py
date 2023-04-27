# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

number1 = int(input('Введите число A: '))
number2 = int(input('Введите число B: '))


def exponentiation(number1, number2):
    if number2 == 1:
        return number1
    if number2 == 0:
        return 1
    return number1 * exponentiation(number1, number2 - 1)


if number1 < 0 or number2 < 0:
    print('Нужно вводить числа больше 0')
else:
    print(exponentiation(number1, number2))
