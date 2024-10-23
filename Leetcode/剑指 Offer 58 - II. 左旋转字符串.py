def reverseLeftWords(m: str, n: int):
    x = ""
    z = ""
    for i, v in enumerate(m):
        if i < n:
            x = "".join([x, v])
        else:
            z = "".join([z, v])
    z = "".join([z, x])
    return z


if __name__ == "__main__":
    s = "abcdefg"
    k = 2
    x = reverseLeftWords(s, k)
    print(x)
