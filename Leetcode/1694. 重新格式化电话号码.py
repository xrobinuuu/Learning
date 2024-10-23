def reformatNumber(number: str) -> str:
    number = number.replace(" ", "")
    number = number.replace("-", "")
    j, k = divmod(len(number), 3)
    s = str()
    for i in range(j):
        s = "-".join([s, number[i * 3: 3 * (i + 1)]])
    if k == 1:
        s = "-".join([s[:-4], s[-3:-1], number[-2:]])
    elif k == 0:
        s = s
    else:
        s = "-".join([s, number[-2:]])
    return s[1:]


if __name__ == "__main__":
    Number = "1-23-45 6"
    y = reformatNumber(Number)
    print(y)
