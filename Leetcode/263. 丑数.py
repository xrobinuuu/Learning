def isUgly(n: int) -> bool:
    while 1:
        if -1 < n <= 5:
            return True
        elif n % 2 == 0:
            n //= 2
        elif n % 3 == 0:
            n //= 3
        elif n % 5 == 0:
            n //= 5
        else:
            return False


if __name__ == '__main__':
    N = 0
    y = isUgly(N)
    print(y)
