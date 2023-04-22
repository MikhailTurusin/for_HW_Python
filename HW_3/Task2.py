# Задача 18:
# Требуется найти в массиве A самый близкий по величине элемент к заданному числу X.
# Если таких элементов несколько, вы вывести один любой.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию).
# Последняя строка содержит число X

# *Пример:*

# 5
#     7 -2 3 5 1
#     6
#     -> 7

from random import randint

number = int(input("Введите размер массива: "))

list = [randint(-15, 15) for _ in range(number)]
print(*list)
list.sort()

number1 = int(input("Задайте желаемое число: "))
res = list[0]
for i in range(number):
    if list[i] <= number1:
        res = list[i]
    else:
        print(f"Ближайший элемент к числу {number1} это число {res}")
        break
else:
    print(f"Ближайший элемент к числу {number1} это число {res}")
