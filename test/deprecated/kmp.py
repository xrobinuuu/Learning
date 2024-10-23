def kmp_next(s):
    kmp_ls = [0]
    for i, v in enumerate(s[1:], 1):
        ind = kmp_ls[-1]
        if v == s[ind]:
            kmp_ls.append(kmp_ls[-1] + 1)
        else:
            kmp_ls.append(0)

    return kmp_ls

    # kmp_ls = [0]
    # ind = 1
    # cur = 0
    # lt = len(s)
    # while ind < lt:
    #     if s[cur] == s[ind]:
    #         cur += 1
    #         ind += 1
    #         kmp_ls.append(cur)
    #     elif cur:
    #         cur = kmp_ls[cur - 1]
    #     else:
    #         kmp_ls.append(0)
    #         ind += 1
    # return kmp_ls

    # res = list()
    # i = 0
    # while i < len(s):


def search(main, lesser):
    # ind = 0
    # pos = 0
    # kmp = kmp_next(lesser)
    # while ind < len(main):
    #     if main[ind] == lesser[pos]:
    #         ind += 1
    #         pos += 1
    #     elif pos:
    #         pos = kmp[pos - 1]
    #     else:
    #         ind += 1
    #
    #     if pos == len(lesser):
    #         print(ind - pos)
    #         pos = kmp[pos - 1]
    m_len = len(main)
    l_len = len(lesser)
    kmp = kmp_next(lesser)
    m = ind = 0
    while ind < l_len and m < m_len:
        if main[m] == lesser[ind]:
            ind += 1
            m += 1
        elif ind:
            ind = kmp[ind - 1]
        else:
            m += 1
    m_ind = [m - l_len, m - 1] if ind == l_len else False

    return m_ind


if __name__ == "__main__":
    Main = "aaabagcxsa"
    Lesser = "aabag"

    y = search(Main, Lesser)
    print(y)
