def reverseBits(n: int):
    return int(bin(n)[2:].rjust(32, "0")[::-1], 2)


if __name__ == '__main__':
    N = '11111111111111111111111111111101'
    N = int(N, 2)
    y = reverseBits(N)
    print(y)


open()