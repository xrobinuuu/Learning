def isSymmetric(root):
    # def metric(p, q):
    #     if p is None and q is None:
    #         return True
    #     if (p is not None and q is None) or (p is None and q is not None) or (q.val != p.val):
    #         return False
    #
    #     return metric(p.left, q.right) and metric(p.right, q.left)
    #
    # if root is None:
    #     return False
    #
    # return metric(root.left, root.right)

    def tree1(root, res):
        if root is None:
            res.append(None)
            return
        res.append(root.val)
        tree1(root.left, res)
        tree1(root.right, res)

    def tree2(root, res):
        if root is None:
            res.append(None)
            return
        res.append(root.val)
        tree2(root.right, res)
        tree2(root.left, res)


    res1 = []
    res2 = []
    tree1(root.left, res1)
    tree2(root.right, res2)
    return res1 == res2
