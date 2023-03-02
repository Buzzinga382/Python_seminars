# Задача 1: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго
# множества. Затем пользователь вводит сами элементы множеств. (Попробуйте использовать множества и их пересечение)

# import random
#
# first_list = [random.randint(-100, 100) for _ in range(int(input('Enter number of elements in first list: ')))]
# second_list = [random.randint(-100, 100) for _ in range(int(input('Enter number of elements in second list: ')))]
#
# print('First list: ', first_list)
# print('Second list: ', second_list)
#
# first_set = set(first_list)
# second_set = set(second_list)
#
# new_set = first_set.intersection(second_set)
# new_list = list(new_set)
# print('Intersection of two lists: ', new_list)

# First method:

# temp = 0
# for i in range(len(new_list)):
#     for j in range(len(new_list) - i):
#         if new_list[j + i] < new_list[i]:
#             temp = new_list[i]
#             new_list[i] = new_list[j + i]
#             new_list[j + i] = temp
#
# print('Result list: ', new_list)

# Second method:

# new_list.sort()
# print('Result list: ', new_list)

################################################################################


# Задача 2: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора
# на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# import random
#
# blackberry_bushes = [random.randint(0, 10) for _ in range(int(input('Enter number of bushes: ')))]
# print(blackberry_bushes)
#
# sum = 0
# max1 = 0
#
# for i in range(len(blackberry_bushes) - 2):
#     sum = blackberry_bushes[i] + blackberry_bushes[i + 1] + blackberry_bushes[i + 2]
#     if sum > max1:
#         max1 = sum
#
# max2 = blackberry_bushes[-1] + blackberry_bushes[0] + blackberry_bushes[1]
# max3 = blackberry_bushes[-2] + blackberry_bushes[-1] + blackberry_bushes[0]
#
# new_list = [max1, max2, max3]
#
# print(max(new_list))

