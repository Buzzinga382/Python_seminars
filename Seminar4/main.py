# Задача 1. Напишите программу, которая принимает на вход строку,
# и отслеживает кол-во повторов каждого символа.

# First method

# some_string = input('Enter your string: ')
# used_set = set()
# for letter in some_string:
#     if letter not in used_set:
#         print(f'{letter} - {some_string.count(letter)}')
#     used_set.add(letter)

# Second method

# some_string = input('Enter your string: ')
# letter_count_dict = {}
# for letter in some_string:
#     if letter not in letter_count_dict:
#         letter_count_dict[letter] = 1
#     else:
#         letter_count_dict[letter] += 1
# print(letter_count_dict)


# Задача 2. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки. Определите, сколько различных
# слов содержится в этом тексте.

# First method

# some_string = input('Enter your string: ')
# words_set = set()
# word = ''
# for i in some_string:
#     if i not in {' ', '.', ',', '!', '?'}:
#         word += i
#     else:
#         if word != '':
#             words_set.add(word)
#         word = ''
# print(len(words_set))

# Second method

# a = 'some things that    i wanna test. tist tis test'
# a_list = a.split()
# print(len(set(a_list)))


