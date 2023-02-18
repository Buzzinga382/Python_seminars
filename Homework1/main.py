# Задача 1: Найдите сумму цифр трехзначного числа.
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


# Var1:

# n = int(input('Please enter 3-digit number: '))
#
# if -100 < n < 100 or n < -999 or n > 999:
#     print('Incorrect input')
#     exit()
#
# if n < 0:
#     n = -n
#
# print('Sum of digits equals: ', (n % 10) + (n % 100)//10 + (n % 1000)//100)


# Var2:

# n = input('Please enter 3-digit number: ')
#
# if n[0] == '-' and len(n) != 4:
#     print('Incorrect input')
#     exit()
#
# elif n[0] != '-' and len(n) != 3:
#     print('Incorrect input')
#     exit()
#
# else:
#     if n[0] == '-':
#         print('Sum of digits equals: ', int(n[1]) + int(n[2]) + int(n[3]))
#     else:
#         print('Sum of digits equals: ', int(n[0]) + int(n[1]) + int(n[2]))

################################################################################


# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

# Var1

# s = int(input('Please enter the total number of cranes: '))
#
# if s % 6 == 0:
#
#     print('Peter made ', s//6, 'cranes')
#
#     print('Kate made ', s//3 * 2, 'cranes')
#
#     print('Serey made ', s//6, 'cranes')
#
# else:
#     print('Peter made ', s // 6, 'cranes')
#
#     print('Kate made ', (s // 6 * 4) + (s % 6), 'cranes')
#
#     print('Serey made ', s // 6, 'cranes')

# Var2

# s = int(input('Please enter the total number of cranes: '))
#
# if s % 6 == 0:
#
#     print('Peter made ', s//6, 'cranes')
#
#     print('Kate made ', s//3 * 2, 'cranes')
#
#     print('Serey made ', s//6, 'cranes')
#
# else:
#     print("They can't made this number of cranes")


################################################################################


# Задача 3: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались
# за проезд и получали билет с номером. Счастливым билетом называют такой билет
# с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

# n = input('Please enter ticket number: ')
#
# if len(n) != 6:
#     print('There is no a ticket number')
#     exit()
#
# else:
#
#     sum1 = int(n[0]) + int(n[1]) + int(n[2])
#     sum2 = int(n[3]) + int(n[4]) + int(n[5])
#     if sum1 == sum2:
#         print('Congrats! You are lucky!')
#
#     else:
#         print('Sorry, maybe other time...')


################################################################################

# Задача 4: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по прямой между
# дольками (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

# n = int(input("Size of chocolate's first side: "))
# m = int(input("Size of chocolate's second side: "))
#
# k = int(input("How much pieces you wanna break off?: "))
#
# if k == m * n:
#     print('This is the whole chocolate, dude!')
#     exit()
#
# elif k > m * n or k < 1:
#     print("Impossible to break of this number of pieces")
#
# else:
#     if k % m == 0 or k % n == 0:
#         print('Yes, you can break off this number of pieces')
#
#     else:
#         print("No, you can't break off this number of pieces")

################################################################################




