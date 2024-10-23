def addBinary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    A = "11"
    B = "1"
    y = addBinary(A, B)
    print(y)
