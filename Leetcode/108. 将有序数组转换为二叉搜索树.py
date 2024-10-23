class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def sortedArrayToBST(nums):
    def bst(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = bst(left, mid - 1)
        root.right = bst(mid + 1, right)
        return root

    return bst(0, len(nums) - 1)

    # n = len(nums)
    # if not n:
    #     return None
    # return TreeNode(nums[n // 2], sortedArrayToBST(nums[0: n // 2]), sortedArrayToBST(nums[n // 2 + 1:]))


if __name__ == "__main__":
    Nums = [-10, -3, 0, 5, 9]

    r = sortedArrayToBST(Nums)
    print(r)
