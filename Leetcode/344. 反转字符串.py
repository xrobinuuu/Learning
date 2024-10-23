def reverseString(s: list[str], x="dd"):
    # s.reverse()
    for i in range(len(s) // 2):
        s[i], s[(i + 1) * -1] = s[(i + 1) * -1], s[i]


if __name__ == "__main__":
    S = ["h", "e", "l", "l", "o"]
    reverseString(S)
    print(S)
