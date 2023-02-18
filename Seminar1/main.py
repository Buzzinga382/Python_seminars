# 1. Посчитайте сумму трех введенных целых чисел

# a = int(input('Please enter first number: '))
# b = int(input('Please enter second number: '))
# c = int(input('Please enter third number: '))

# print()
# print('Sum of this numbers is: ', a + b + c)


# 2. Даны два целых числа: A, B. Проверить истинность высказывания: "Числа A и B имеют одинаковую четность"

# a = int(input('Please enter A number: '))
# b = int(input('Please enter B number: '))

# if a % 2 == b % 2:
#     print('Yes')

# else:
#     print('No')


# 3. Пользователь вводит два целых числа. Выведите меньшее из них.

# a = int(input('Please enter first number: '))
# b = int(input('Please enter second number: '))

# if a > b:
#     print(b)

# elif a == b:
#     print('Numbers are equal')

# else:
#     print(a)


# 4. Пользователь вводит целое число. Выведите YES,
# если это число является четырехзначным, и NO в противном случае.

# a = int(input('Please enter some number: '))

# if 999 < a < 10000 or -10000 < a < -999:
#     print('Yes')

# else:
#     print('No')


# 5. За день машина проезжает n километров. Сколько дней нужно,
# чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

# n = int(input('Please enter N number: '))
# m = int(input('Please enter M number: '))

# print('You will need', (-m//n)*-1, 'days')


# 5. В некоторой школе решили набрать три новых математических класса и оборудовать
# кабинеты для них новыми партами. За каждой партой может сидеть два учащихся.
# Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт,
# которое нужно приобрести для них.


a = int(input('How much students in first room: '))
b = int(input('How much students in second room: '))
c = int(input('How much students in third room: '))

print('You will need', (-a//2)*-1 + (-b//2)*-1 + (-c//2)*-1, 'tables')


