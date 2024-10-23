def addDigits(num: int) -> int:
    while num and num > 9:
        s = str(num)
        num = 0
        for v in s:
            num += int(v)
    return num


if __name__ == '__main__':
    Num = 0
    y = addDigits(Num)
    print(y)
