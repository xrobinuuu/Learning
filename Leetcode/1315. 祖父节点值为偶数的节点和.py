import math


def sumevengrandparent(root: list):
    null = 0
    # root.
    # total = 0
    # for i, v in enumerate(root, 1):
    #     if v % 2 == 0 and 4 * i < len(root):
    #         total += sum(root[4 * i - 1: 4 * (i + 1) - 1])
    #
    # return total
    for i in root:
        print(i)


null = 0


class Solution:
    def __init__(self):
        self.res = 0

    def sumEvenGrandparent(self, root, lev1, lev2):
        def recursion(root: TreeNode, lev2: int, lev1: int):
            if root:
                recursion(root.left, lev1, root.val)
                recursion(root.right, lev1, root.val)

                if lev2 % 2 == 0 and lev2 != 0:
                    self.res += root.val

        recursion(root, 0, 0)
        return self.res


class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def gen_tree(ls, n=0):
    if n >= len(ls) or ls[n] is None:
        return None
    return TreeNode(val=ls[n], left=gen_tree(ls, 2 * n + 1), right=gen_tree(ls, 2 * n + 2))


if __name__ == "__main__":
    val_ls = [6, 7, 8, 2, 7, 1, 3, 9, null, 1, 4, null, null, null, 5]
    val_ls2 = [61, 13, 46, null, null, null, 56, 72]
    root = gen_tree(val_ls2)
    print(root.left.val)
    y = Solution().sumEvenGrandparent(root, 0, 0)
    print(y)
    # print(root.val)
    # print(int(math.log2(10)))
