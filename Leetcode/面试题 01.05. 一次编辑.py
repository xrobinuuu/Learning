def oneEditAway(first: str, second: str) -> bool:
    indf = len(first) - 1
    inds = len(second) - 1
    d = indf - inds
    if -1 < d < 1:
        return False
    if first == "" or second == "":
        return True
    cot = 2
    while cot and inds >= 0 and indf >= 0:
        if first[indf] != second[inds]:
            cot -= 1
            if abs(d):
                if d == 1:
                    indf -= 1
                elif d == -1:
                    inds -= 1
                continue
        indf -= 1
        inds -= 1
    if cot < 1:
        return False
    return True


if __name__ == '__main__':
    f = "ab"
    g = "bc"
    x = oneEditAway(f, g)
    print(x)
