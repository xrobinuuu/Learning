def removeElements(head, val: int):
    # while head and head.val == val:
    #     head = head.next
    # node = head
    # while head and head.next:
    #     if head.next.val == val:
    #         head.next = head.next.next
    #         continue
    #     head = head.next
    # return node

    while head and head.val == val:
        head = head.next
    node = head
    while head and head.next:
        if head.next.val == val:
            head.next = head.next.next
        else:
            head = head.next
    return node
