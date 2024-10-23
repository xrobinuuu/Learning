def firstPalindrome(words: list[str]) -> str:
    for i in words:
        x = len(i) // 2
        if i[:x] == i[-1 * x:][::-1] or x == 0:
            return i
    return ""


if __name__ == "__main__":
    Words = ["def", "ghi"]
    y = firstPalindrome(Words)
    print(y)
