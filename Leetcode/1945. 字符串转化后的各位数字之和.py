def getLucky(s: str, k: int) -> int:
    num = str()
    for i in s:
        num += str(ord(i) - 96)
    while k:
        j = 0
        for v in num:
            j += int(v)
        num = str(j)
        k -= 1
    return int(num)


if __name__ == "__main__":
    S = "zbax"
    K = 2
    y = getLucky(S, K)
    print(y)
