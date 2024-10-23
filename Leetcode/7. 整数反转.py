# def reverse(x):
#     x = str(x)
#     if x.startswith("-"):
#         return print(foo(x.strip("-")) * -1)
#     else:
#         return print(foo(x))
#
#
# def foo(x):
#     y = ""
#     for i in range(len(x)):
#         y += x[len(x) - 1 - i]
#         print(y)
#     y = int(y)
#     if (-2 ** 31) < y < ((2 ** 31) - 1):
#         return y
#     else:
#         return 0
# def reverse(x):
#     x = str(x)
#     y = ""
#     for i in range(len(x)):
#         y += x[len(x) - 1 - i]
#     if x.startswith("-"):
#         y = int(y.strip("-")) * -1
#     else:
#         y = int(y)
#     if (-2 ** 31) < y < ((2 ** 31) - 1):
#         return print(y)
#     else:
#         return 0
#
#


# def reverse(x):
#     a = str(x)
#     li = list()
#     for i in range(len(a)):
#         li.insert(0, a[i])
#     b = ''.join(li)
#     if b.endswith("-"):
#         b = ''.join(['-', b.strip("-")])
#     return int(b)

# def reverse(num):
#     print(num, end="/")
#     num = str(num)[::-1]
#     print(num)
#     try:
#         return int(num)
#     except ValueError:
#         return -int(num[:-1])
#
#
# if __name__ == '__main__':
#     import time
#     import numpy as np
#
#     case = np.random.randint(-1000, 1000, 1000)
#     t_1 = time.perf_counter()
#     for n in case:
#         x = reverse(n)
#     t_2 = time.perf_counter()
#     print(t_2 - t_1)

print("-123"[::-1])

