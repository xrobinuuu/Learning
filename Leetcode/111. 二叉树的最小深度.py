def minDepth(root):
    def depth(node, n):
        if node is None:
            return
        if node.left is None and node.right is None:
            res.append(n + 1)
            return
        n += 1
        depth(node.left, n)
        depth(node.right, n)
    if root is None:
        return 0
    res = []
    depth(root, 0)
    return min(res)

