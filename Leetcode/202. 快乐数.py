def isHappy(n: int) -> bool:
    q = str(n)
    h = set()
    while q:
        num = 0
        for i in q:
            i = int(i)
            num += i * i
        print(num)
        if num == 1:
            return True
        if q in h:
            return False
        h.add(q)
        q = str(num)


if __name__ == "__main__":
    N = 2
    y = isHappy(N)
    print(y)
