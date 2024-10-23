def to_bin(n, m):
    if n < 0 and abs(n) <= 2 ** (m - 1):
        res = bin((abs(n) ^ ((2 ** m) - 1)) + 1)[2:]
    elif 0 <= n <= 2 ** (m - 1) - 1:
        res = bin(n)[2:].rjust(m, "0")
    else:
        raise Exception(f'整型溢出{m}位二进制')
    return res


def cal(a, b, m):
    r = bin(int(a, 2) + int(b, 2))[2:]
    return r[len(r) - m:]


if __name__ == "__main__":
    i = 9
    j = -10
    x = to_bin(i, 64)
    print(x)
    y = to_bin(j, 64)
    print(y)
    z = cal(x, y, 64)
    print(z)

    print(int(z, 2))
    print(i + j)
