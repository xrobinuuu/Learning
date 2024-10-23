def isIsomorphic(s: str, t: str) -> bool:
    vst = {}
    se = set()
    for i, v in enumerate(s):
        if v in vst:
            if vst[v] != t[i]:
                return False
            continue
        if t[i] in se:
            return False
        vst.update({v: t[i]})
        se.add(t[i])
    return True


if __name__ == '__main__':
    S = "egr"
    T = "add"

    y = isIsomorphic(S, T)
    print(y)
