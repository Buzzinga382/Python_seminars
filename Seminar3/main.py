# import time
#
# some_list = []
# count = 0
# for _ in range(10 ** 6):
#     some_list.append(count)
#     count += 1
#
# some_set = set()
# count = 0
# for _ in range(10 ** 6):
#     some_set.add(count)
#     count += 1
#
#
# find_number = 999998
# start = time.perf_counter()
# print(find_number in some_list)
# end = time.perf_counter()
# a = end - start
#
# start = time.perf_counter()
# print(find_number in some_set)
# end = time.perf_counter()
# b = end - start
# print(a / b)


################################################################################


# Задача 1. Дан список чисел. Определите, сколько в нем встречается различных чисел.

# some_list = [1, 4, 5, 9, 34, 75, 4, 5]
#
# some_set = set(some_list)
# print(len(some_set))


# Задача 2. Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# # на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# new_list = [int(input()) for _ in range(int(input('Enter number of elements: ')))]
# print(new_list)
#
# k = int(input('Enter some number: '))
# other_list = new_list[k:] + new_list[:k]
#
# print(other_list)


# Задача 3. Напишите программу для печати всех уникальных значений в словаре.

# new_dict = {1: 3, 5: 38, 2: 3}
#
# a = new_dict.values()
#
# new_set = set(a)
#
# print(new_set)



# Задача 4. Дан массив, состоящий из целых чисел. Напишите программу,
# которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим индексом)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# our_list = [int(input()) for _ in range(int(input('Enter number of elements: ')))]
#
# count = 0
# for i in range(0, len(our_list) - 1):
#     if our_list[i + 1] > our_list[i]:
#         count += 1
#
# print(count)



# Задача 5. Формат ввода
# Вводится количество играющих, затем строки, в которых могут быть их имена.
# Затем вводится количество имен и сами имена детей для поиска.
#
# Формат вывода
# Для каждого имени выведите номер строки (счет с 1), в которой оно первый
# раз встретилось, или -1, если такого имени не было.
#
# Пример ввода
# 7
# Bessy kept the garden gate,
# And Mary kept the pantry.
# Little Betty Blue Lost her holiday shoe.
# Billy, Billy, come and play.
# Yes, my Polly, so I will.
# Little Bobby Snooks was fond of his books.
# Robert Barnes, my fellow fine, can you shoe this horse of mine?
# 4
# Mary
# Jack
# Billy
# Bobby
#
# Вывод
# 2
# -1
# 4
# 6


# n = int(input('Введите количество играющих: '))
# new_list = []
#
#
# for _ in range(n):
#     sentence = input()
#     new_list.append(sentence)
#
# m = int(input('Введите количество имён: '))
#
#
# for _ in range(m):
#     name = input()
#     flag = False
#     for i in range(len(new_list)):
#         if name in new_list[i]:
#             print(i + 1)
#             flag = True
#             break
#     if not flag:
#         print(-1)


# Задача с собеседования! Есть список чисел, вводят некое число n. Нужно понять, есть ли в списке
# такие 2 различных числа, что их сумма будет равна числу n.


import time
import random

some_list = [random.randint(1, 10000) for _ in range(10 ** 6)]

start = time.perf_counter()
n = int(input('Enter some number: '))
flag = True
for i in some_list:
    if n - i in some_list:
        print(i, n - i)
        break
else:
    print('НЕТ')
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
some_set = set(some_list)
flag = True
for i in some_list:
    if n - i in some_set:
        print(i, n - i)
        break
else:
    print('НЕТ')
end = time.perf_counter()
print(end - start)



