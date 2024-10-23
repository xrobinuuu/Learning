def diff_fig(n):
    total = 10 ** n


def cs(n):
    if n == 0:
        return 1
    tmp = 9
    for i in range(n - 1):
        tmp *= (9 - i)
    return tmp + cs(n - 1)


# def plus1(ls):
#     if not ls:
#         return [1]
#     tmp = (ls[-1] + 1) % 10
#     if tmp == 0:
#         return plus1(ls[:-1]) + [tmp]
#     return ls[:-1] + [tmp]

def plus1(ls):
    tmp = int(''.join(map(str, ls)))
    return list(map(int, list(str(tmp))))


def plus2(ls: list):
    lis = []
    while 1:
        if not ls:
            return [1] + lis[::-1]
        k = (ls.pop() + 1) % 10
        lis.append(k)
        # k = 0 if (ls.pop() + 1) % 10 == 0 else ls.pop() + 1
        # if not ls:
        #     lis.append(1)
        #     return ls + lis[::-1]
        if k != 0:
            return ls + lis[::-1]


if __name__ == "__main__":
    # x = cs(4)
    # print(x)
    l = [9, 9, 3, 9]
    x = plus2(l)
    print(x)
