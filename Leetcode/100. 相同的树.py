class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def plant_tree(leaf, n=0):
    if n >= len(leaf) or leaf[n] is None:
        return None
    return TreeNode(val=leaf[n], left=plant_tree(leaf, 2 * n + 1), right=plant_tree(leaf, 2 * n + 2))


def isSameTree(p, q):
    # if p is None and q is None:
    #     return True
    # if (p is not None and q is None) or (p is None and q is not None) or (q.val != p.val):
    #     return False
    #
    # return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

    def tree(root, res):
        if root is None:
            res.append(None)
            return
        res.append(root.val)
        tree(root.left, res)
        tree(root.right, res)

    res1 = []
    res2 = []
    tree(p, res1)
    tree(q, res2)
    print(res1)
    print(res2)
    return res1 == res2


if __name__ == "__main__":
    P = [1, 2]
    Q = [1, None, 2, None, None, None, 3]
    root1 = plant_tree(P)
    root2 = plant_tree(Q)
    x = isSameTree(root1, root2)
    print(x)
