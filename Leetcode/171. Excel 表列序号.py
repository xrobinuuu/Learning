import math
import string


def titleToNumber(co):
    su = 0
    for i, v in enumerate(co[::-1]):
        su += (ord(v) - 64) * pow(26, i)
    return su


def d_2_h(n, f):
    fig_map = dict(zip([i for i in range(10, f)], string.ascii_uppercase[:f - 10]))
    if not n:
        return str()
    j, k = divmod(n, f)
    if k > 9:
        k = fig_map.get(k)
    return d_2_h(j, f) + str(k)


def h_2_d(n, f):
    fig_map = dict(
        zip("".join([str(i) for i in range(10)]) + string.ascii_uppercase[:f - 10], [i for i in range(0, f)]))
    # su = 0
    # for i, v in enumerate(n[::-1]):
    #     su += fig_map.get(v) * pow(f, i)
    # return su
    if not n:
        return 0
    # return fig_map.get(n[0])
    return f * h_2_d(n[:-1], f) + fig_map[n[-1]]


def cal(d, num):
    v = math.ceil(math.log2(num))
    tmp_first = d >> v
    tmp_last = bin((d << (64 - v)))[2:]
    tmp_last = tmp_last[len(tmp_last) - 64:].rjust(64, '0')
    tmp_last = int(tmp_last, 2) >> (64 - v)
    tmp_last = (pow(2, v) - num) * tmp_first + tmp_last
    if tmp_last == d:
        return tmp_first + 1, tmp_last - num
    if tmp_last < num:
        return tmp_first, tmp_last
    return tmp_first + cal(tmp_last, num)[0], cal(tmp_last, num)[1]


if __name__ == "__main__":
    ColumnTitle = "AZN"  # output 2147483647
    x = titleToNumber(ColumnTitle)
    print(x)
    #
    # y = d_2_h(796, 20)
    # print(y)
    #
    # z = h_2_d("1JG", 20)
    # print(z)

    x = 191321
    # print(x % 5)
    # print(x // 5, x >> 3)
    # b_x = bin(x)[2:].rjust(64, '0')
    # print(b_x)
    # y = x << 64 -
    # b_y_t = bin(y)[2:].rjust(64, "0")
    # b_y = b_y_t[len(b_y_t) - 64:].rjust(64, '0')
    # print(b_y)
    # y = int(b_y, 2)
    # print(y)
    # z = y >> 61
    # print(z)
    f, lt = cal(x, 13)
    f_1, lt_1 = divmod(x, 13)
    print(f, lt)
    print(f_1, lt_1)
