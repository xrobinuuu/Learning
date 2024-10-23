def isPalindrome(head) -> bool:
    ls = []
    while head:
        ls.append(head.val)
        head = head.next
    j, k = divmod(len(ls), 2)
    return ls[:j] == ls[j + k:]