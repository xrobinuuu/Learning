def longestPalindrome(s: str) -> str:
    # while ind + end < ext:
    # s1 = s[ind:]
    # e = end
    # print("s1----------->", s1)
    # for i, v in enumerate(s1, 1):
    #     j, k = divmod(end + i, 2)
    #     left, right = s1[ind:j], s1[j + k: end + i]
    #     print(i, j, k, left, right, end)
    #     if left == right[::-1] and left and right:
    #         res = max(res, 2 * j + k)
    #         e = i - 1
    # end += e
    # ind += 1
    if len(set(list(s))) == len(s):
        return s[0]
    ind = 0
    res = str()
    ext = len(s)
    while ind < ext:
        r = len(res)
        for i, v in enumerate(s[ind: ext - r], 1):
            j, k = divmod(r + i, 2)
            left, right = s[ind: ind + j], s[ind + j + k: ind + r + i]
            if left == right[::-1] and left and right:
                res = s[ind: ind + r + i] if len(res) < (r + i) else res
        ind += 1
    if len(s) > 0 and not res:
        res = s[0]
    return res


if __name__ == "__main__":
    S = "ab"

    y = longestPalindrome(S)
    print(y)
