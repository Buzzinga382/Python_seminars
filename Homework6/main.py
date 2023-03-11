# Задача 1:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


# n = int(input('Enter number of elements: '))
# a1 = int(input('Enter first element: '))
# d = int(input('Enter difference: '))
#
# def progression(n, a1, d):
#     new_list = []
#     for i in range(1, n + 1):
#         new_list.append(a1 + (i - 1) * d)
#     return new_list
#
# print(progression(n, a1, d))

################################################################################


# Задача 2: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)


# import random
#
# minn = int(input('Enter minimum range value: '))
# maxx = int(input('Enter maximum range value: '))
#
# some_list = [random.randint(0, 15) for _ in range(int(input('Enter number of elements: ')))]
# print(some_list)
# print()
# for i in range(len(some_list)):
#     if some_list[i] <= maxx and some_list[i] >= minn:
#         print(i)

################################################################################


# Задача 3. Для введенных строк определите, в какой из них встречается больше всего различных
# символов, отличающихся от контрольного. Выведите эти символы из строки без повторений,
# каждый с новой строки. Если таких строк несколько, выведите символы из любой.
# Формат ввода
# Вводится контрольный символ, затем количество строк, затем сами строки.
# Формат вывода
# Выведите подряд без повторений символы из строки, в которой их оказалось больше всего,
# не считая контрольный. Если ни одной не оказалось, выведите -1. Порядок вывода произвольный.
# Пример 1
# Ввод
#
# E
# 5
# EVERY
# MAN
# TO
# HIS
# TASTE
# Вывод
# RVY
# Пример 2
# Ввод
#
# A
# 4
# AA
# AAA
# AAAA
# AAAAAA
# Вывод
# -1


# n = input('Enter your symbol: ')
# some_list = [input('Enter your string: ') for _ in range(int(input('Enter number of strings: ')))]
# new_list = []
# for i in range(len(some_list)):
#     new_list.append(some_list[i].replace(n, ''))
# print(new_list)
# maxx = 0
# res = ''
# for el in range(len(new_list)):
#     if len(new_list[el]) > maxx:
#         maxx = len(new_list[el])
#         res = new_list[el]
#
# if res == '':
#     print(-1)
# else:
#     print(res)








