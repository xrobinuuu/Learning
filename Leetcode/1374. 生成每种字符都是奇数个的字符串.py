def generateTheString(n: int) -> str:
    tmp = divmod(n, 2)
    res = "a" * (n - 1) + "b"
    if tmp[1] == 1:
        res = "c" + res[1:]
    return res


if __name__ == "__main__":
    N = 0
    y = generateTheString(N)
    print(y)
