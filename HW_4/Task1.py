# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

# Пользователь вводит 2 числа.
# n — кол-во элементов первого множества.
# m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

from random import randint

n = int(input("Введите размер 1го списка: "))
m = int(input("Введите размер 1го списка: "))

list1 = [randint(-5, 25) for _ in range(n)]
list2 = [randint(-5, 25) for _ in range(m)]

count1 = set(list1)
count2 = set(list2)
print(count1)
print(count2)

result = count1.intersection(count2)
result1 = sorted(result)
print(result1)
