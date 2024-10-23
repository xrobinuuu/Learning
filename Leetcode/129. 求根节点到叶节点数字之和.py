class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

    def __str__(self):
        return str(self.val)


def plant(rt_ls, n=0):
    if n >= len(rt_ls) or rt_ls[n] is None:
        return None
    return TreeNode(val=rt_ls[n], left=plant(rt_ls, 2 * n + 1), right=plant(rt_ls, 2 * n + 2))


def sumNumbers(root: TreeNode) -> int:
    def to_sum(node, num=0):
        if not node:
            return 0
        figur = num * 10 + node.val
        if node.left is None and node.right is None:
            return figur
        return to_sum(node.left, figur) + to_sum(node.right, figur)
    return to_sum(root)


if __name__ == "__main__":
    # Root_ls = [4, 9, 0, 5, 1]  # output = 1026
    Root_ls = [0, 1]  # output = 50
    rt = plant(Root_ls)

    x = sumNumbers(rt)
    print(x)
