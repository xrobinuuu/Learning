import numpy as np


def minDeletionSize(strs: list[str]) -> int:
    cot = 0
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if strs[j][i] < strs[j - 1][i]:
                cot += 1
                break
    return cot


if __name__ == '__main__':
    Strs = ["rrjk",
            "furt",
            "guzm"]

    y = minDeletionSize(Strs)
    print(y)
