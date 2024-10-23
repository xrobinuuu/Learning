def balancedStringSplit(s: str) -> int:
    ind = 0
    res = 0
    ret = 0
    target = s[0]
    for i, v in enumerate(s):
        if target == v:
            ind += 1
        if target != v:
            res += 1
        if ind == res and ind != 0 and res != 0:
            ret += 1
            if i < len(s) - 1:
                target = s[i + 1]
            ind, res = 0, 0

    return ret


if __name__ == "__main__":
    S = "RLRRRLLRLL"
    balancedStringSplit(S)
