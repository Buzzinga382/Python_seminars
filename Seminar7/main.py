# map:

# some_list = [1, 2, 3, 4, 5, 6, 7]
#
# def square(n):
#     return n ** 2
#
# new_list = list(map(square, some_list))      # or new_list = list(map(lambda n: n ** 2, some_list))
#
# print(new_list)


# filter:

# some_list = [1, 2, 3, 4, 5, 6, 7]
# new_list = list(filter(lambda x: x % 2 == 0, some_list))
# print(new_list)


# zip:

# a = [1, 2, 3]
# b = ['1', '2', '3']
#
# print(list(zip(a, b)))


# enumerate

# number = [10, 223, 123, 43, 12]
# print(list(enumerate(number)))

################################################################################

# Задача 1. У вас есть код, который вы не можете менять(так часто бывает,
# когда код в глубине программы используется множество раз и вы не хотите ничего сломать):
#
# transformation = <???>
#
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
#
# transormed_values = list(map(transformation, values))
#
# Единственный способ вашего взаимодействия с этим кодом - посредством задания функции transformation.
#
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать список значений,
# а нужно получить его как есть.
#
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился копией values.


# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transormed_values = list(map(lambda n: n, values))
# print(transormed_values)

################################################################################

# Задача 2. Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет
# ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте:
# вы знаете, что у вашей звезды таких
# планет нет, зато искусственные спутники были были запущены на круговые орбиты.
# Результатом функции должен быть кортеж,
# содержащий длины полуосей эллипса орбиты самой далекой планеты.
# Каждая орбита представляет из себя кортеж из пары
# чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле
# S = piab, где a и b - длины полуосей эллипса.
# При решении задачи используйте списочные выражения. Подсказка:
# проще всего будет найти эллипс в два шага: сначала
# вычислить самую большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая
# далекая планета ровно одна

# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# def find_farthest_orbit(orbits: list):
#     maxx = orbits[0]
#     for el in orbits:
#         if el[0] != el[1]:
#             if el[0] * el[1] > maxx[0] * maxx[1]:
#                 maxx = el
#     return maxx
#
#
# print(*find_farthest_orbit(orbits))

################################################################################

# Задача 3. Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.


# values = [0, 2, 10, 6]
#
# def same_by(characteristic, objects):
#     if len(objects) == 0:
#         return True
#     characteristic_list = list(map(characteristic, objects))
#     for ind in range(len(list(map(characteristic, objects))) - 1):
#         if characteristic_list[ind] != characteristic_list[ind + 1]:
#             return False
#     return True
#
# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')

################################################################################

# Задача 4. Создайте список из случайных чисел. Найдите номер его последнего локального
# максимума (локальный максимум — это элемент, который больше любого из своих соседей).

# import random
#
# some_list = [random.randint(0, 100) for _ in range(0, 10)]
# print(some_list)
#
# for i in range(len(some_list) - 2, 0, -1):
#     if some_list[i - 1] < some_list[i] > some_list[i + 1]:
#         print(i + 1)
#         break
# else:
#     print("There's no local maximum")

################################################################################


# Задача 5. Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.

# import random
# import  time
# some_list = [random.randint(0, 10) for _ in range(0, 10000000)]
#
#
# start = time.perf_counter()
# max_count = 0
# used_set = set()
# for i in some_list:
#     if i not in used_set:
#         count = some_list.count(i)
#         if some_list.count(i) > max_count:
#             max_count = count
#         used_set.add(i)
# end = time.perf_counter()
# res_1 = end - start
# print(max_count)
#
#
# start2 = time.perf_counter()
# our_dict = {}
#
# for i in some_list:
#     if i not in our_dict:
#         our_dict[i] = 1
#     else:
#         our_dict[i] += 1
#
# max_counter = max(our_dict.values())
# end2 = time.perf_counter()
# print(max_counter)
# res_2 = end2 - start2
#
# print(res_1 / res_2)

################################################################################


# Задача 6. Создайте список из случайных чисел. Найдите второй максимум.

# import random
# import  time
# some_list = [random.randint(0, 10) for _ in range(0, 10)]
# print(some_list)
# some_list = list(set(some_list))
#
#
# first_max = some_list[0]
# second_max = some_list[1]
#
# if first_max < second_max:
#     first_max, second_max = second_max, first_max
#
# for i in range(2, len(some_list)):
#     if some_list[i] > first_max:
#         first_max, second_max = some_list[i], first_max
#     elif some_list[i] > second_max:
#         second_max = some_list[i]
#
# print(second_max)

################################################################################

















