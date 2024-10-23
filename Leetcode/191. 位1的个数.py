def hammingWeight(n) -> int:
    # s = 0
    # z = bin(n)[2:]
    # k = z.count("1")
    # print(k)
    # for i in range(len(z)):
    #     s += int(z[i])
    # return s

    # s = 0
    # z = bin(n)[2:]
    # for i in z:
    #     if i == "1":
    #         s += 1
    # return s

    ret = 0
    while n:
        n &= n - 1
        ret += 1
    return ret


x = "00000000000000000000000000001011"
y = int(x, 2)
j = hammingWeight(y)
print(j)
