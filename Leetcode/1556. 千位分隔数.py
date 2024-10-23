import re


def thousandSeparator(n: int) -> str:
    s = str(n)[::-1]
    j = len(s) % 3
    if j:
        j = [s[-j:]]
    else:
        j = []
    k = re.findall(".{3}", s)
    k.extend(j)
    return ".".join(k)[::-1]


if __name__ == "__main__":
    N = 0
    x = thousandSeparator(N)
    print(x)
