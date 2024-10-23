import re
import string
import pandas as pd


def mostCommonWord(p: str, b: list[str]) -> str:
    p = p.lower()
    while b:
        x = b.pop()
        p = p.replace(x, "")
    p = re.findall(r"\w+", p)
    maxd = dict()
    for v in set(p):
        maxd.update({p.count(v): v})
    return maxd[max(maxd)]

    # df = pd.DataFrame({'alphe': p})
    # df['c'] = 1
    # alphe = df.groupby("alphe").sum()
    # return alphe.stack().idxmax()[0]
    # print(alphe)
    #
    #
    # print()

    # while p:
    #     j = p[0]
    #     maxu.update({p.count(j): j})
    #     p.remove(j)


if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    x = mostCommonWord(paragraph, banned)
    print(x)
