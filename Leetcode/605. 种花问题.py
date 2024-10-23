def canPlaceFlowers(flowerbed, n):
    # res = 0
    # tmp = 0
    # for i in flowerbed:
    #     if i == 1 and tmp:
    #         res += (tmp - 1) // 2
    #         tmp = 0
    #     if i == 0:
    #         tmp += 1
    # res += (tmp - 1) // 2
    # return res >= n

    res = 1
    tmp = 0
    ex = len(flowerbed)
    for i, v in enumerate(flowerbed):
        if v == 0:
            res += 1
        if v == 1 or ex - 1 == i:
            j, k = divmod(res, 2)
            tmp += j - 1 + k
            if k == 0 and v == 0:
                tmp += 1
            res = 0
    return tmp >= n


if __name__ == "__main__":
    F = [0, 0, 1, 0, 1, 0, 0, 0, 0]
    N = 1
    y = canPlaceFlowers(F, N)
    print(y)
