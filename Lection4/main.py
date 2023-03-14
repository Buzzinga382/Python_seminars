# def calc1(a, b):
#     return a + b
# def calc2(a, b):
#     return a * b
#
# calc3 = lambda a, b: a + b
#
# def math(op, x, y):
#     print(op(x, y))
#
# math(calc3, 5, 45)
#
# math(lambda a, b: a + b, 5, 45)

################################################################################

some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_list = []
#
# for i in range(len(some_list)):
#     if some_list[i] % 2 == 0:
#         new_list.append((some_list[i], some_list[i]**2))
#
# print(new_list)

# def select(f, list_1):
#     return [f(x) for x in list_1]
#
# def where(f, list_1):
#     return [x for x in list_1 if f(x)]
#
# res = select(int, some_list)
# print(res)
# res = where(lambda x: x % 2 == 0, res)
# print(res)
# res = list(select(lambda x: (x, x**2), res))
# print(res)

################################################################################

# list_1 = [x for x in range(1, 20)]
# print(list_1)
#
# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)

################################################################################

# data = [15, 65, 9, 36, 175]
#
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)



