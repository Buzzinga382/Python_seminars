# Задача 1. Напишите функцию read_last(lines, file), которая будет открывать
# определенный файл file и выводить на печать построчно последние строки
# в количестве lines (на всякий случай проверим, что задано положительное целое число).
# Протестируем функцию на файле «article.txt» со следующим содержимым:
#
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела

# with open('article.txt', 'w', encoding='utf-8') as file:
#     text = ['Вечерело', 'Жужжали мухи', 'Светил фонарик', 'Кипела вода в чайнике',
#             'Венера зажглась на небе', 'Деревья шумели', 'Тучи разошлись', 'Листва зеленела']
#     for el in text:
#         file.write(el + '\n')
#
# def read_last(lines, file):
#     with open(file, 'r', encoding='utf-8') as res:
#         if lines < 0:
#             print('Incorrect input!')
#         text = res.read().splitlines()
#         for i in range(len(text) - lines, len(text)):
#             print(text[i])
#
# lines = int(input('Enter number of last lines: '))
#
# read_last(lines, 'article.txt')


################################################################################


# Задача 2. Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
# Требуется реализовать функцию longest_words(file), которая записывает в файл
# result.txt слово, имеющее максимальную длину (или список слов, если таковых несколько).


# def longest_words(file):
#     with open(file, 'r', encoding='utf-8') as new_file:
#         text = new_file.read().splitlines()
#         new_list = []
#         list2 = []
#         res_list = []
#         for i in range(len(text)):
#             new_list.append(text[i].split())
#         for j in new_list:
#             for k in j:
#                 list2.append(k)
#         maxx = 0
#         for el in list2:
#             res_list.append(len(el))
#         for num in range(len(res_list)):
#             maxx = max(res_list)
#         for elem in list2:
#             if len(elem) == maxx:
#                 with open('result.txt', 'a', encoding='utf-8') as res_file:
#                     res_file.write(elem + '\n')
#
# longest_words('article.txt')

# def pivotIndex(nums):
#     left_and_right_sum = 0
#     total_sum = sum(nums)
#     for i in range(len(nums)):
#         if nums[i] == total_sum - left_and_right_sum * 2:
#             return i
#         left_and_right_sum += nums[i]
#     else:
#         return -1

def pivotIndex(nums):
    left_sum, right_sum = 0, sum(nums)

    for ind, el in enumerate(nums):
        right_sum -= el
        if left_sum == right_sum:
            return ind
        left_sum += el

    return -1


list1 = [-1,-1,1,1,0,0]

print(pivotIndex(list1))
