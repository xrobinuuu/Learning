def longestCommonPrefix(strs):
    i = 0
    v = ""
    while 1:
        if len(strs) == 1:
            return strs[0]
        else:
            for k in strs[1:]:
                if len(k) > 0 and len(strs[0]) > 0:
                    if i <= len(k) and i <= len(strs[0]) and k[i] == strs[0][i]:
                        continue
                    else:
                        return v
                else:
                    return v
            v += strs[0][i]
            i += 1


print(longestCommonPrefix(["ab", "a"]))



