# Задача 6. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
# *Примеры:*
# - 6,78 -> 7
# - 5 -> нет
# - 5,00 -> нет

from math import*
a = float(input())

if a - floor(a) != 0:
    print(floor(a * 10)% 10)
else:
    print('Дробной части нет!')