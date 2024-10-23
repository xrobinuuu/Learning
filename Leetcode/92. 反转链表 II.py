class ListNode:
    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next

    def __str__(self):
        return str(self.val)


def list_node(ln):
    if not ln:
        return None
    return ListNode(val=ln[0], _next=list_node(ln[1:]))


def reverseBetween(head):
    node = ListNode()
    node.next = head
    pre = node.next
    while pre.next:
        # cur = pre.next
        # _next = cur.next
        # cur.next = node.next
        # node.next = cur
        # pre.next = _next
        tmp, pre.next.next, node.next = pre.next.next, node.next, pre.next
        pre.next = tmp
    return node.next


if __name__ == '__main__':
    he = [1, 2, 3, 4, 5, 6, 8, 10]
    le = 3
    ri = 8
    hea = list_node(he)
    y = reverseBetween(hea)
    while y:
        print(y.val, end=',')
        y = y.next