def getKthFromEnd(head, k):
    tmp, i, j = head, 0, head
    while 1:
        if j is None:
            return tmp
        if i > k - 1:
            tmp = tmp.next
        j = j.next
        i += 1


if __name__ == "__main__":
    pass
