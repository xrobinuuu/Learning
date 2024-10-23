import numpy as np


def s(t):
    t_nda = np.array(t)
    return np.sum(t_nda > 0) + np.sum(np.append(np.max(t_nda, axis=0), np.max(t_nda, axis=1)))


def projectionArea(t) -> int:
    f = t[0]
    res = 0
    for i in t:
        h = 0
        for ind, j in enumerate(i):
            if j > f[ind]:
                f[ind] = j
            if j > h:
                h = j
            if j > 0:
                res += 1
        res += h
    res += sum(f)
    return res


def area(t):
    # res = 0
    # for i in range(len(t[0])):
    #     h = 0
    #     for j in range(len(t)):
    #         res += bool(t[j][i])
    #         if t[j][i] > h:
    #             h = t[j][i]
    #         if i == 0:
    #             res += max(t[j])
    #     res += h
    # return res

    # k = t[0] + [len(t[0]) * len(t)]
    # for g in t:
    #     k[-1] += max(g)
    #     for i, val in enumerate(g):
    #         if not val:
    #             k[-1] -= 1
    #         k[i] = max(k[i], val)

    k = t[0] + [len(t[0]) * len(t)]
    while t:
        j = t.pop(0)
        k[-1] += max(j)
        i = 0
        while j:
            g = j.pop(0)
            if not g:
                k[-1] -= 1
            k[i] = max(k[i], g)
            i += 1

    return sum(k)


if __name__ == "__main__":
    x = [[1, 2], [3, 4]]
    # x = [[2]]
    y = s(x)
    # z = projectionArea(x)
    v = area(x)
    print(y)
    # print(z)
    print(v)
