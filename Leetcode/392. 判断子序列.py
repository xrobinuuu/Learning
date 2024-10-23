def isSubsequence(s: str, t: str) -> bool:
    a = set(s)
    b = set(t)
    c = a | b

    return len(c) == len(b)


if __name__ == "__main__":
    S = "acb"
    T = "ahbgdc"
    x = isSubsequence(S, T)
    print(x)
