import ListNode as L


def reverseBetween( head, left: int, right: int):
    if left == right:
        return head
    arr = []
    start, end = None, None
    cur = head
    count = 1
    while cur:
        if count + 1 == left:
            start = cur
        if count == right + 1:
            end = cur
        if count >= left and count <= right:
            arr.append(cur.val)
        cur = cur.next
        count += 1

    dummy = L.ListNode(None)
    cur = dummy
    while len(arr):
        cur.next = L.ListNode(arr.pop())
        cur = cur.next

    if start == None:
        head = dummy.next
    else:
        start.next = dummy.next
    if end != None:
        cur.next = end
    return head

if __name__ == '__main__':
    foo = L.ListNode()
    linkedList = foo.produce([1,2,3,4,5])
    reverseBetween(linkedList, 1, 5)