from collections import defaultdict


def min_tree(ls):
    visited = set()
    # while ls:
    #     leaf = ls.pop()
    #     a, b = leaf[0], leaf[1]
    #     visited[a].append(b)
    #     visited[b].append(a)
    #
    # print(visited)
    tree = set()
    for i in ls:
        a, b = i[0], i[1]


if __name__ == "__main__":
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]

    min_tree(edges)
