# Задача 1. Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве,
# затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве.
# Затем элементы второго массива

import random
#
# first_list = [random.randint(1, 10) for _ in range(int(input('Enter size of the first list: ')))]
# second_list = {random.randint(1, 10) for _ in range(int(input('Enter size of the second list: ')))}
#
# print(first_list)
# print(second_list)
#
# for i in first_list:
#     if i not in second_list:
#         print(i)

################################################################################


# Задача 2. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве
# определит количество элементов, у которых два соседних и, при этом, оба соседних элемента
# меньше данного. Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# some_list = [random.randint(1, 15) for _ in range(int(input('Enter size of the first list: ')))]
# print(some_list)
# count = 0
# for i in range(1, len(some_list) - 1):
#     if some_list[i] > some_list[i - 1] and some_list[i] > some_list[i + 1]:
#         count += 1
#
# print(count)


################################################################################


# Задача 3. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

# Пример:

# 3 3 4 5 6 3 -> 1
# 3 3 4 5 3 6 3 -> 2
# 3 3 4 4 5 5 3 1 6 3 -> 4

# First method

# our_list = [random.randint(1, 15) for _ in range(int(input('Enter size of the first list: ')))]
# print(our_list)
# used_set = set()
# amount = 0
#
# for i in our_list:
#     if i not in used_set:
#         amount += our_list.count(i) // 2
#         used_set.add(i)
#
# print(amount)


# Second method

# our_list = [random.randint(1, 15) for _ in range(int(input('Enter size of the first list: ')))]
# count_dict = {}
#
# for i in our_list:
#     if i not in count_dict:
#         count_dict[i] = 1
#     else:
#         count_dict[i] += 1
#
# amount = 0
# for value in count_dict.values():
#     amount += value // 2
#
# print(amount)


################################################################################


# Задача 4. Два различных натуральных числа n и m называются дружественными, если сумма
# делителей числа n (включая 1, но исключая само n) равна числу m и наоборот.
# Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары
# дружественных чисел, каждое из которых не превосходит k. Программа получает на
# вход одно натуральное число k, не превосходящее 10 в 5 степени. Программа должна вывести все
# пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить
# по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз
# (перестановка чисел новую пару не дает).


def find_sum_div(num):
    summa = 0
    for div in range(1, num // 2 + 1):
        if num % div == 0:
            summa += div
    return summa


some_dict = {}
k = int(input('Enter number K: '))
for number in range(1, k + 1):
    if number in some_dict:
        if find_sum_div(number) == some_dict[number]:
            print(number, some_dict[number])
    some_dict[find_sum_div(number)] = number

    