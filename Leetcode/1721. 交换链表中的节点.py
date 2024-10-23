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


def swapNodes(head, k: int):
    node = pre = head
    for _ in range(k - 1):
        head = head.next
    fir = head
    while head.next:
        pre = pre.next
        head = head.next
    fir.val, pre.val = pre.val, fir.val
    return node


if __name__ == '__main__':
    h = [1, 2]
    k1 = 2
    he = list_node(h)
    y = swapNodes(he, k1)
    print("----------")
    for _ in range(len(h)):
        print(y, end=",")
        y = y.next
    print(h)
