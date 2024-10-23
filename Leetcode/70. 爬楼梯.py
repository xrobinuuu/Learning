import math


def climbStairs(n: int) -> int:
    # x1, x2, res = 0, 0, 1
    # for i in range(n):
    #     x1 = x2
    #     x2 = res
    #     res = x1 + x2
    # return res

    sq = math.sqrt(5)
    fib = math.pow((1 + sq) / 2, n + 1) - math.pow((1 - sq) / 2, n + 1)
    return round(fib / sq)


if __name__ == "__main__":
    N = 4
    y = climbStairs(N)
    print(y)
