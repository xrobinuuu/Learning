def lengthOfLongestSubstring(s):
    # sls = s[1:]
    # for v in sls:
    #     if s[0] == v:
    #         j = sls.index(v) + 1
    #         k = lengthOfLongestSubstring(sls)
    #         if k is None:
    #             k = 0
    #         print(j, k, sls)
    #         return max(j, k)
    # if s is None:
    #     return 0
    # if s[0] in s[1:]:
    #     j = s[1:].index(s[0]) + 1
    #     k = 1 + lengthOfLongestSubstring(s[1:])
    #     return max(j, k)
    # else:
    #     return len(s[1:])

    # if not s:
    #     return
    # i, di = 0, len(s)
    # while i != di and i < di:
    #     if s[i] in s[i + 1:]:
    #         di = i + s[i + 1:].index(s[i]) + 1
    #         break
    #     i += 1
    # return min(di, lengthOfLongestSubstring(s[i + 1:]))

    if not s:
        return 0
    i, di, rec = 0, len(s), -1
    while i != di:
        if s[i] in s[i + 1: di]:
            di, rec = i + s[i + 1:].index(s[i]) + 1, i
        i += 1
    return max(di, lengthOfLongestSubstring(s[rec:][1:]))


if __name__ == "__main__":
    S = "abba"
    x = lengthOfLongestSubstring(S)
    print(x)
