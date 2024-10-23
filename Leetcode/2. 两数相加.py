from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def _iterate_node(node: Optional[ListNode]):
            number = ''
            while node:
                number += str(node.val)
                node = node.next
            return int(number[::-1])

        return self.generate_list_node(list(map(int, str(_iterate_node(l1) + _iterate_node(l2))[::-1])))

    def generate_list_node(self, li: List):
        if not li:
            return None
        return ListNode(val=li.pop(0), next=self.generate_list_node(li))


if __name__ == '__main__':
    _l1 = [2, 4, 3]
    _l2 = [5, 6, 4]
    l1_node = Solution().generate_list_node(_l1)
    l2_node = Solution().generate_list_node(_l2)

    Solution().addTwoNumbers(l1_node, l2_node)

