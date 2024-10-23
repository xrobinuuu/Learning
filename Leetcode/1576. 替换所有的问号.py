def modifyString(s: str) -> str:

    if len(s) < 2:
        return s
    st = s[0]
    if st == "?":
        st = ord(s[-2]) + 2
        if st > 123:
            st -= 5
        st = chr(st)
    for i in range(1, len(s) - 1):
        if s[i] == "?":
            j = ord(s[i - 1]) - 2
            if chr(j) == s[i + 1]:
                j -= 2
            while j < 97 or j > 123 or chr(j) == s[i + 1]:
                if j > 97:
                    j += 13
                else:
                    j -= 15
            st += chr(j)
        else:
            st += s[i]
    end = s[-1]
    if end == "?":
        end = ord(s[-2]) + 2
        if end > 123:
            end -= 5
        end = chr(end)
    st += end
    return st


def ms(s):
    # i = 0
    # les = len(s)
    # while i < les:
    #     if s[i] == '?':
    #         tmp_1 = i - 1
    #         tmp_2 = i + 1
    #         tmp = 'abc'
    #         if tmp_1 >= 0:
    #             tmp = tmp.replace(s[tmp_1], "")
    #         if tmp_2 < les:
    #             tmp = tmp.replace(s[tmp_2], "")
    #         tmp_3 = tmp[0]
    #         s = s.replace('?', tmp_3, 1)
    #     i += 1
    # return s
    i = 0
    les = len(s)
    res = str()
    while i < les:
        if s[i] == '?':
            tmp_2 = i + 1
            tmp = 'abc'
            if tmp_2 < les:
                tmp = tmp.replace(s[tmp_2], "")
            if res:
                tmp = tmp.replace(res[-1], "")
            res += tmp[0]
        else:
            res += s[i]
        i += 1
    return res


if __name__ == '__main__':
    S = "j?qg??b"
    # y = modifyString(S)
    # print(y)
    y = ms(S)
    print(y)
