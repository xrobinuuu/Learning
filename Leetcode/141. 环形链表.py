def hasCycle(head):
    # vst = set()
    # while head:
    #     if head in vst:
    #         return True
    #     vst.add(head)
    #     head = head.next
    # return False
    if not head:
        return False
    while head.next and head.next.next:
        if head.next == head.next.next:
            return True
        head = head.next
        head.next = head.next.next
    return False
