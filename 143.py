import ListNode as L

def reorderList(head):
    # find the mid element
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the second half list
    pre, cur, nex = None,slow.next,None
    while cur:
        nex,cur.next = cur.next, pre
        pre,cur = cur,nex
    slow.next = None

    # merge two list
    l1, l2 = head, pre
    while l2:
        l1.next, l1 = l2, l1.next
        l2.next, l2 = l1, l2.next

    return head

if __name__ == '__main__':
    listnode = L.ListNode()
    head = listnode.produce([1,2,3])
    ans = reorderList(head)