def strStr(haystack: str, needle: str) -> int:
    if not haystack and not needle:
        return 0
    if needle in haystack:
        ls = haystack.split(needle, 1)
        return len(ls[0])
    return -1


if __name__ == "__main__":
    Haystack = ""
    Needle = ""
    y = strStr(Haystack, Needle)
    print(y)
