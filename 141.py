import ListNode as L

def isHasCycle(head):
    slow, fast = head, head
    while slow != fast and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    if fast == None or fast.next == None:
        return False
    else:
        return True

if __name__ == '__main__':
    listnode = L.ListNode()
    head = listnode.produce([1,2])
    ans = isHasCycle(head)