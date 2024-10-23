import re


def reversePrefix(word: str, ch: str) -> str:
    x = re.match(f"[^{ch}]*{ch}", word)
    x = "" if not x else x.group()[::-1]
    return x + word[len(x):]


if __name__ == "__main__":
    Word = "xyxzxe"
    Ch = "z"
    y = reversePrefix(Word, Ch)
    print(y)
