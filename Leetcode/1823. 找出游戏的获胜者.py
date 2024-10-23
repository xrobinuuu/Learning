def findTheWinner(n: int, k: int) -> int:
    q, flat = list(range(1, n + 1)), -1
    while len(q) != 1:
        flat = (k + flat) % len(q)
        del q[flat]
        flat -= 1
    return q[0]


if __name__ == "__main__":
    N = 5
    K = 2
    y = findTheWinner(N, K)
    print(y)
