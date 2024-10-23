
def juest(n):
    for i in range(10, 100):
        for k in range(10, 100):
            if i * k == n:
                return [i, k]


if __name__ == "__main__":
    x = 9000

    y = juest(x)
    print(y)

