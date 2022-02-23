import ListNode as L


def insertionSortList(head):
    cur = head
    dummy = L.ListNode(None)
    while cur:
        if cur == head:
            dummy.next = L.ListNode(head.val)
        else:
            tmp, pre = dummy.next, dummy
            while tmp and cur.val > tmp.val:
                pre = tmp
                tmp = tmp.next
                
            newNode = L.ListNode(cur.val)
            pre.next, newNode.next = newNode, tmp
        cur = cur.next
    return dummy.next

if __name__ == '__main__':
    listnode = L.ListNode()
    head = listnode.produce([4,2,1,3])
    ans = insertionSortList(head)