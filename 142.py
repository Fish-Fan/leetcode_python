import ListNode as L


def detectCycle(head):
    if head == None or head.next == None:
        return None
    slow, fast = head.next, head.next.next
    slowCount, fastCount = 1, 2
    while slow != head and fast and fast.next:
        if slow == fast:
            break
        slow = slow.next
        fast = fast.next.next
        slowCount += 1
        fastCount += 2
    if fast == None or fast.next == None:
        return None
    cycleLength = fastCount - slowCount

    tmp, n = head, 0
    while n != cycleLength:
        n += 1
        tmp = tmp.next

    start, end = head, tmp
    while start != end:
        start = start.next
        end = end.next
    return start

if __name__ == '__main__':
    listNode = L.ListNode()
    head = listNode.producewithcycle([3,2,0,4], 1)
    ans = detectCycle(head)
