# Задача 10:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

# 5 -> 1 0 1 1 0
# 2

import random

number = int(input("Введите количество монет: "))
min = 0
max = 1
countmin = 0
countmax = 0

for _ in range(number):
    temp = random.randint(0, 1)
    print(temp, end=" ")
    if temp == max:
        countmax += 1
    else:
        countmin += 1
if countmin < countmax:
    print()
    print(countmin)
else:
    print()
    print(countmax)
