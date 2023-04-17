# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

number = int(input("Введите число: "))

count = 0

while 2**count < number:
    print(2**count, end=" ")
    count += 1
