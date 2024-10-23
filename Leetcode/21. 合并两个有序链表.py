def mergeTwoLists(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val > l2.val:
        l2.next = mergeTwoLists(l1.next, l2)
    else:
        l1.next = mergeTwoLists(l1, l2.next)


