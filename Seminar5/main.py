# def hello(name='stranger'):
#     print('Hello', name)
#
# hello()

# def hello(name='stranger'):
#     return f'Hello {name}'
#
# print(hello('Alex'))


# def hello(*name_list):
#     for name in name_list:
#         print('Hello', name)
#
# hello('Alex', 'Anton', 'Ann')

################################################################################

# Задача 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
#
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#
# Требуется найти N-е число Фибоначчи

# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)
#
# print(fib(6))


################################################################################

# Задача2. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
#  5, 5, 4, 2, 3, 4, 5 -> 2, 2, 4, 2, 3, 4, 2


# def changer(*marks):
#     res = searcher(marks)
#     minn, maxx = res[0], res[1]
#     marks = list(marks)
#
#     for i in range(len(marks)):
#         if marks[i] == maxx:
#             marks[i] = minn
#
#     return marks
#
#
# def searcher(marks):
#     max_number = marks[0]
#     min_number = marks[0]
#
#     for i in marks:
#         if i < min_number:
#             min_number = i
#         if i > max_number:
#             max_number = i
#
#     return min_number, max_number
#
# print(changer(5, 5, 3, 2, 4, 4, 5, 2, 3))

################################################################################


# Задача 3. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
#
# *Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)*

# n = int(input('Enter your number: '))
#
# def is_simple_number(n):
#     for i in range(2, n // 2 + 1):
#         if n % i == 0:
#             return "Number isn't simple"
#
#     return "Number is simple"
#
# res = is_simple_number(n)
# print(res)

################################################################################

# Задача 4. Заданы три множества идентификаторов – человек болел, сделал 2 прививки, имеет медотвод.
# Если его идентификатор есть хотя бы в одном из множеств, то ему нужно выдать QR-код.
#
# Напишите программу, которая будет это проверять.
#
# Формат ввода
# Три раза вводятся числа (идентификаторы), пока не будет введена пустая строка.
# Затем вводится количество запросов и сами запросы.
#
# Формат вывода
# Вывести все запросы (по одному в строке), которые есть хотя бы в одном из множеств,
# без повторений, порядок вывода произвольный.
#
# 123
# 231
# 301
#
# 301
# 200
#
# 222
# 212
#
# 3
# 221
# 123
# 301
#
#
# Вывод:
#     123
#     301


# big_set = set()
#
# for _ in range(3):
#     while True:
#         id = input()
#         if not id:      # то есть если не айди, то есть пустая строка, то есть уже не True
#             break
#
#         big_set.add(id)
#
# n = int(input('Enter number of requests: '))
#
# for _ in range(n):
#     find_id = input('Enter request: ')
#     if find_id in big_set:
#         print(find_id)



