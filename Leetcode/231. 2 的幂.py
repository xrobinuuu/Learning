import math


def isPowerOfTwo(n: int) -> bool:
    if n < 1:
        return False


    return n == pow(2, int(math.log2(n)))


y = isPowerOfTwo(-16)
print(y)
