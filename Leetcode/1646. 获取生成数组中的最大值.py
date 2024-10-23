import math


def getMaximumGenerated(n: int):
    ls = [0, 1, 1]
    i = 3
    if n < 3:
        return max(ls[:n + 1])
    while i < n + 1:
        tmp = divmod(i, 2)
        num = ls[tmp[0]] + (tmp[1] * ls[tmp[0] + 1])
        ls.append(num)
        i += 1
    return max(ls)

    # ls = [0, 1]
    # i = 2
    # if n == 0:
    #     return 0
    # while i < n + 1:
    #     tmp = divmod(i, 2)
    #     num = ls[tmp[0]] + (tmp[1] * ls[tmp[0] + 1])
    #     ls.append(num)
    #     i += 1
    # return max(ls)


if __name__ == "__main__":
    N = 7
    y = getMaximumGenerated(N)
    print(y)
