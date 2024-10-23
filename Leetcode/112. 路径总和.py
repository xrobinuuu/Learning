def hasPathSum(root, target):
    if root is None:
        return False
    if root.left is None and root.right is None:
        return target == root.val

    return hasPathSum(root.left, target - root.val) or hasPathSum(root.right, target - root.val)



