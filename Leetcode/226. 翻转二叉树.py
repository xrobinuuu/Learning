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


def invertTree(root):
    if not root:
        return None

    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root


if __name__ == '__main__':
    r = [4, 2, 7, 1, 3, 6, 9]
    ro = plant_tree(r)

    y = invertTree(ro)
    print(y.left.right)
