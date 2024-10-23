def wordPattern(pattern: str, s: str) -> bool:
    ls = s.split(" ")
    visited = dict()
    pats = set()
    for i, v in enumerate(pattern):
        if v not in visited and ls[i] not in pats:
            visited.update({v: ls[i]})
            pats.add(ls[i])
        else:
            if ls[i] in pats and visited.get(v) == ls[i]:
                continue
            return False
    return True


if __name__ == "__main__":
    pattern = "abba"
    str = "dog cat cat dog"
    y = wordPattern(pattern, str)
    print(y)
