# Задача 1:
# Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# Первый вариант решения через числа:

number = int(input("Введите число: "))
sum = 0
while number > 0:
    sum += number % 10
    number //= 10
print(sum)

# Второй вариант решения через строки:

# number=(input("Введите число: "))
# print(int(number[0])+int(number[1])+int(number[2]))