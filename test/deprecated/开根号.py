import math
import time


def sqrt_fun(n, k):
    # n = n * 10**k
    i = n / 2
    while i ** 2 > n:
        if i ** 2 > n:
            return i - 1 + (n - (i - 1) ** 2) / (2 * (i - 1))
        if i ** 2 == n:
            return i


# def sqrt(n):
#     z = n
#     while z ** 2 > n:
#         tmp = (z ** 2 + n) / (2 * z)
#         if z == tmp:
#             break
#         z = tmp
#     return (z ** 2 + n) / (2 * z)


def sqrt(n):
    return int(math.exp(math.log(n) / 2))


if __name__ == "__main__":
    x = 6666
    # y = sqrt_fun(x, 14)
    # print(y, math.sqrt(x))
    # for x in range(1, 100):
    #     y = sqrt(x)
    #     y_std = math.sqrt(x)
    #     t = abs((x - y ** 2) * 10 ** 15) == abs((x - y_std ** 2) * 10 ** 15)
    #     if not t:
    #         print(x, abs((x - y ** 2) * 10 ** 15), abs((x - y_std ** 2) * 10 ** 15))

    y = sqrt(x)
    y_std = math.sqrt(x)
    print(y)
    print(y_std)
