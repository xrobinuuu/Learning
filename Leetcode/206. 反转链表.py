def reverseList(head):

    first = head
    while head and head.next:
        node = head.next
        head.next = head.next.next
        node.next = first
        first = node
    return first

