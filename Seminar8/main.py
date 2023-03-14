# with open('example.txt', 'r', encoding='utf-8') as file:
    # text = file.read()
    # print(text)

    # line = file.readline()
    # while line:
    #     print(line)
    #     line = file.readline()

    # text = file.read().splitlines()
    # print(text)

    # text = file.readlines()
    # print(text)

# with open('res.txt', 'w', encoding='utf-8') as file:
#     res = [1, 2, 4, 5, 6, 8]
#     for el in res:
#         file.write(str(el) + '\n')

################################################################################

# Задача 1. Пользователь вводит название файла и символ, найти количество таких
# символов в файле и результат записать в файл res.txt

# name = input('Enter file name: ')
# symbol = input('Enter symbol: ')
# count = 0
# with open(name, 'r', encoding='utf-8') as file:
#     text = file.read()
#     for letter in text:
#         if symbol == letter:
#             count += 1
#
# with open('res.txt', 'w', encoding='utf-8') as file:
#     file.write(str(count))

################################################################################

# Задача 2. Дан текстовый файл, вывести список из предпоследних слов в строках,
# индексы которых кратны 3, если в строке 1 слово,
# то выводим -1.
# Результаты вывести в файл res.txt

# name = input('Enter file name: ')
# with open(name, 'r', encoding='utf-8') as file:
#     with open('res.txt', 'w', encoding='utf-8') as res:
#         text = file.read().splitlines()
#         for i in range(len(text)):
#             if i % 3 == 0:
#                 a = text[i].split()
#                 if len(a) > 1:
#                     res.write(a[-2] + '\n')
#                 else:
#                     res.write('-1' + '\n')
#             else:
#                 res.write('0' + '\n')


################################################################################


# Задача 3. Есть 2 файла, их нужно объединить в один (создав третий)

# with open('example1.txt', 'w', encoding='utf-8') as res:
#     with open('example.txt', 'r', encoding='utf-8') as file2:
#         line = file2.readline()
#         while line:
#             res.write(line)
#             line = file2.readline()
#         res.write('\n')
#     with open('ex2.txt', 'r', encoding='utf-8') as file3:
#         line = file3.readline()
#         while line:
#             res.write(line)
#             line = file3.readline()

################################################################################


# Задача 4. Дан текстовый файл с некоторым количеством строк, в каждой из которых записано целое число.
# Вводится число. Нужно найти такие числа из файла, которые в сумме дают вводимое число.

# n = int(input('Enter some number: '))
#
# with open('example.txt', 'r', encoding='utf-8') as file:
#     text = file.read().splitlines()
# some_set = set(text)

# First method:

# for i in some_set:
#     for j in some_set:
#         if (int(i) + int(j)) == n:
#             print(i, j)

# Second method:

# for i in some_set:
#     if n - int(i) in some_set:
#         print(int(i), n - int(i))


