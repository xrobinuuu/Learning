import math
from collections import Counter


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def plant_tree(leaf, n=0):
    if n >= len(leaf) or leaf[n] is None:
        return None
    return TreeNode(val=leaf[n], left=plant_tree(leaf, 2 * n + 1), right=plant_tree(leaf, 2 * n + 2))


def full_tree_to_list(node):
    q = [node]
    tree_ls = list()
    i = 0
    n = 0
    while q:
        i += 1
        n = int(math.log2(i))
        node = q.pop(0)
        if node is None:
            tree_ls.append(None)
            q.append(None)
            q.append(None)
        else:
            tree_ls.append(node.val)
            q.append(node.left)
            q.append(node.right)
        if Counter(tree_ls[int(math.pow(2, n) - 1): int(math.pow(2, n + 1))])[None] == math.pow(2, n):
            break
    return tree_ls[: int(math.pow(2, n) - 1)]


def simple_tree_to_list(node):
    q = [node]
    tree_ls = list()
    while q:
        node = q.pop(0)
        if node is None:
            tree_ls.append(None)
            continue
        tree_ls.append(node.val)
        q.append(node.left)
        q.append(node.right)
    return tree_ls


def ls_gen_root(num_ls):
    index_ls = [0, 1]
    i = 0
    while index_ls[i + 1] < len(num_ls):
        tmp_ls = num_ls[index_ls[i]: index_ls[i + 1]]
        tmp_index = index_ls[i + 1] + 2 * (len(tmp_ls) - Counter(tmp_ls)[None])
        index_ls.append(tmp_index)
        i += 1
    index_ls = index_ls[::-1]
    under = num_ls[index_ls[1]: index_ls[0]]
    many = 2 * (len(under) - Counter(under)[None])
    tmp_root = [None] * many
    res = list()
    i = 1
    print(index_ls)
    while i < len(index_ls):
        floor = num_ls[index_ls[i]: index_ls[i - 1]]
        j = 0
        for num in floor:
            if num is None:
                res.append(None)
                continue
            res.append(TreeNode(val=num, left=tmp_root[j], right=tmp_root[j + 1]))
            j += 2
        tmp_root, res = res, list()
        i += 1
    return tmp_root[0]


def root_gen_ls(node):
    q = [node]
    tree_ls = list()
    while q:
        node = q.pop(0)
        if node is None:
            tree_ls.append(None)
            continue
        tree_ls.append(node.val)
        q.append(node.left)
        q.append(node.right)
    i = 0
    j = 1
    while j < len(tree_ls):
        tmp_ls = tree_ls[i: j]
        gap = 2 * (len(tmp_ls) - Counter(tmp_ls)[None])
        i, j = j, j + gap
    return tree_ls[: i]


if __name__ == "__main__":
    null = None
    # ls = [6, 7, 8, 2, None, 1, 3, 9, None, None, None, 10, None, None, 5, 1, -1, None, None, None, None, None, None, 3, 7, None, None, None, None, -5, None]
    ls = [6, 7, 8, 8, None, None, 7, 6, None, None, 6]
    root = ls_gen_root(ls)
    print(root.right)

    fh = root_gen_ls(root)
    print(fh)

    # root = plant_tree(ls)
    #
    # print(root.val)

    # y = full_tree_to_list(root)
    # print(y)

    # z = simple_tree_to_list(root)
    # print(z)
