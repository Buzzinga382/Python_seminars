# Задача 1
# Строка представляет собой арифметическое выражение из однозначных чисел и знаков + и -. Вычислите результат.
# Пример
# Ввод
# 8-5+2-1
# Вывод
# 4

# user_str = input('Enter your string: ')
#
# def str_to_formula(some_str):
#     res = 0
#     i = 0
#     flag = True
#     while flag:
#         if some_str[i] == '+':
#             res = res + int(some_str[i - 1]) + int(some_str[i + 1])
#             flag = False
#         elif some_str[i] == '-':
#             res = res + int(some_str[i - 1]) - int(some_str[i + 1])
#             flag = False
#         i += 1
#
#     for i in range(i, len(some_str)):
#         if some_str[i] == '+':
#             res = res + int(some_str[i + 1])
#         elif some_str[i] == '-':
#             res = res - int(some_str[i + 1])
#
#     return res
#
# print(str_to_formula(user_str))


################################################################################


# Задача 2
# Словом в данной задаче считается последовательность букв, ограниченная пробелами или началом или концом строки.
# Выведите все слова из строки в столбик. НЕЛЬЗЯ ПОЛЬЗОВАТЬСЯ МЕТОДАМИ СТРОК (split)
# Формат ввода
# Вводится строка.
# Формат вывода
# Выведите слова из строки по одному.
# Пример 1
# Ввод
#
# Hello, world!
# Вывод
# Hello,
# world!
# Пример 2
# Ввод
#
# My heart in the Highland
# Вывод
# My
# heart
# in
# the
# Highland


# user_string = input('Enter your string: ')
#
# word = ''
#
# for i in user_string:
#     if i not in {' ', '.', ',', '!', '?', ''}:
#         word += i
#     else:
#         if word != '':
#             print(word)
#         word = ''
#
#
# if word != '':
#     print(word)


################################################################################


# Задача 3:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8


# # First method:

# import time
#
# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))
#
# def to_the_power(a, b):
#     if b == 0:
#         return 1
#     elif b == 1:
#         return a
#
#     elif b == 2:
#         return a * a
#     else:
#         return a * to_the_power(a, b - 1)
#
# start = time.perf_counter()
# print(to_the_power(a, b))
# end = time.perf_counter()
# first_time = end - start
#
# # Second method:
#
# def to_the_power_of(a, b):
#     res = 1
#     if b == 0:
#         return 1
#     else:
#         while b >= 1:
#             res = res * a
#             b -= 1
#     return res
#
# start = time.perf_counter()
# print(to_the_power_of(a, b))
# end = time.perf_counter()
# second_time = end - start
#
# print('Recursion sucks this much:', round(first_time / second_time, 2))


################################################################################


# Задача 4: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух
# целых неотрицательных чисел. Из всех арифметических операций допускаются
# только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
#
# 2 2
#     4

# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))
#
# def sum(a, b):
#     if b == 0:
#         return a
#     elif a == 0:
#         return b
#     elif a >= b:
#         return 1 + sum(a - 1, b)
#     elif a < b:
#         return 1 + sum(a, b - 1)
#
# print(sum(a, b))
