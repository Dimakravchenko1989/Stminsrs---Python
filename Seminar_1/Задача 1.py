# Задача 1. Напишите программу, которая принмает на вход два числа и проверяет, является ли одно квадратом другового.
# Пример: 
# 5, 25 - да
# 4, 16 - да
# 25, 5 - да
# 8, 9 - нет

a = int(input('Введите число А:'))
b = int(input('Введите число В:'))

if a == b**2 or b == a**2:
    print('Да')
else:
    print('Нет')

