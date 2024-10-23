def reorderLogFiles(logs):
    def trans(log: str) -> tuple:
        a, b = log.split(' ', 1)
        return (0, b, a) if b[0].isalpha() else (1,)
    logs.sort(key=trans)
    return logs


if __name__ == "__main__":
    Logs = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    y = reorderLogFiles(Logs)
    print(y)

