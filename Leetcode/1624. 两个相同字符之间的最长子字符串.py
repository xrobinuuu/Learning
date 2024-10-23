def maxLengthBetweenEqualCharacters(s: str) -> int:
    res = -1
    vst = dict()
    for i, v in enumerate(s):
        if v in vst:
            res = max(i - vst[v] - 1, res)
        else:
            vst.update({v: i})
    return res


if __name__ == "__main__":
    S = "abca"
    y = maxLengthBetweenEqualCharacters(S)
    print(y)
