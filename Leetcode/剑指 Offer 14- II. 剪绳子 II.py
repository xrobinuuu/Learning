def cuttingRope(n: int):
    # if n == 3:
    #     return 2
    if n <= 3:
        return n - 1
    m, res = divmod(n, 3)
    if res == 2:
        y = 2 * (pow(3, m))
    else:
        y = pow(3, (m - 1)) * (3 + res)
    return divmod(y, 1000000007)[1]


if __name__ == '__main__':
    x = cuttingRope(120)
    print(x)
