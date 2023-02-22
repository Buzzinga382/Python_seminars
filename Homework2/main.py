# Задача 1. На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток, которые
# нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть


# from random import randint
#
# n = int(input('Please enter number of coins: '))
#
# countHeads = 0
# countTales = 0
#
# for i in range(n):
#     coins = randint(0, 1)
#     print(coins, end=' ')
#     if coins == 0:
#         countHeads += 1
#     else:
#         countTales += 1
#
# print()
#
# if countHeads >= countTales:
#     print('You need to flip', countTales, 'coins')
#
# else:
#     print('You need to flip', countHeads, 'coins')

################################################################################


# Задача 2: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих
# чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# import math
#
# s = int(input('Please enter sum of needed numbers: '))
# p = int(input('Please enter product number: '))
#
# x = (s + math.sqrt(s*s - 4*p))/2
#
# y = p/x
#
# print('Peter guessed this numbers: ', x, 'and', y)

################################################################################


# Задача 3: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# n = int(input('Please enter some number: '))
#
# i = 0
# res = 0
#
# while 2**i <= n:
#     res = 2**i
#     print(res, end=' ')
#     i += 1

################################################################################






