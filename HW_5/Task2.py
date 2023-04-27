# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# Пример:
# 2 2
# 4


number1 = int(input("Введите число a: "))
number2 = int(input("Введите число b: "))


def sum1(number1, number2):
    if number2 == 0:
        return number1
    return sum1(number1 + 1, number2 - 1)


if number1 < 0 or number2 < 0:
    print('Нужно вводить числа больше 0')
else:
    print(sum1(number1, number2))
