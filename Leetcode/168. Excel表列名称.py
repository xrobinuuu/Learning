import math
import string


def convertToTitle(n):
    if not n:
        return str()
    j, k = divmod(n - 1, 26)
    return convertToTitle(j) + chr(65 + k)

    # fig_map = dict(zip(range(26), string.ascii_uppercase))
    # j, k = divmod(n - 1, 26)
    # if j == 0:
    #     return fig_map.get(k)
    # return convertToTitle(j) + fig_map.get(k)


z = 1380 - 1
y = convertToTitle(z)
print(y)


def convertToTitle_b(n):
    if not n:
        return str()
    j, k = divmod(n, 26)
    return convertToTitle_b(j) + chr(65 + k)


def cv(s):
    n = math.ceil(math.log(26 + 25 * s, 26) - 2)
    tmp = (pow(26, n + 1) - 1) / 25
    s_1 = int(s - tmp)
    res = convertToTitle_b(s_1)
    return res.rjust(n + 1, 'A')


x = cv(z)
print(x)
print(z // 26, z % 26)
