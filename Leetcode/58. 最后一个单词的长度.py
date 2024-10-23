import re


def lengthOfLastWord(s: str) -> int:
    s = re.findall(r"\w+", s)
    if not s:
        return 0
    return len(s[-1])


if __name__ == "__main__":
    S = ""
    y = lengthOfLastWord(S)
    print(y)
