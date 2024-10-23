import copy
import random


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


def delete_duplicates(head: ListNode):
    # if head is None:
    #     return head
    # q = [head.next]
    # visited = {head.val}
    # position = head
    # while q:
    #     node = q.pop()
    #     if node.next is None:
    #         position.next = None
    #         return head
    #     v = node.val
    #     q.append(node.next)
    #     if v in visited: continue
    #     position.next = node
    #     position = node
    #     visited.add(node.val)

    # if head is None:
    #     return None
    # tem = head.next
    # if tem is not None and head.val == tem.val:
    #     return delete_duplicates(tem)
    # head.next = delete_duplicates(head.next)
    # return head

    # if head is None or head.next is None:
    #     return head
    # tem = head
    # if tem.val == tem.next.val:
    #     tem.next = tem.next.next
    #     return delete_duplicates(tem)
    # else:
    #     tem = tem.next
    #     head.next = delete_duplicates(tem)
    #     return head

    tem = head
    while tem.next:
        if tem.val == tem.next.val:
            tem.next = tem.next.next
        else:
            tem = tem.next
    return head


if __name__ == "__main__":
    # heads = sorted([random.randint(0, 100) for i in range(10)])
    heads = [1, 1, 1, 2, 3, 3]
    print(heads)
    x = list_node(heads)
    y = delete_duplicates(x)

    print(y.next.next.next)












