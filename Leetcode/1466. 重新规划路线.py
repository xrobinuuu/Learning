def minReorder(n: int, connections: list):
    set1 = set()
    set2 = set()
    count = 0
    while connections:
        ls = connections.pop()
        x = ls[0]
        y = ls[1]
        if x in set1:
            set1.add(y)
            set2.add(x)
            count += 1
        else:
            set1.add(x)
            set2.add(y)

    return count


z = minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]])
print(z)
