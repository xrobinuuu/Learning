def maximumTime(time: str) -> str:
    ls = list(time)
    for i in range(len(time)):
        if i == 2 or time[i] != "?": continue
        if i == 0:
            ls[0] = "2" if ls[1] < "4" or ls[1] == "?" else "1"
        elif i == 1:
            ls[1] = "3" if ls[0] == "2" else "9"
        else:
            ls[i] = str(2 * i + 1 - 2 * (i % 2))
    return "".join(ls)


if __name__ == '__main__':
    Time = "??:??"
    y = maximumTime(Time)
    print(y)