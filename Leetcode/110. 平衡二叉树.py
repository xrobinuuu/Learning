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


def isBalanced(root):


    # def balance(node):
    #     if node is None:
    #         return 0
    #     return max(balance(node.left), balance(node.right)) + 1
    # if root is None:
    #     return True
    # return abs(balance(root.left) - balance(root.right)) <= 1 and isBalanced(root.left) and isBalanced(root.right)

    def height(root: TreeNode) -> int:
        if not root:
            return 0
        left = height(root.left)
        right = height(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        else:
            return max(left, right) + 1

    return height(root) >= 0


if __name__ == "__main__":
    ro = [1, None, 2, None, None, None, 3]
    root1 = plant_tree(ro)

    y = isBalanced(root1)
    print(y)
