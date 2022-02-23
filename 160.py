import ListNode as L


def getIntersectionNode( headA, headB):
    # concatenate these two linked list
    cur1 = headA
    while cur1.next:
        cur1 = cur1.next
    cur1.next = headB
    # calculate the length of the cycle
    slow, fast = headA.next, headA.next.next
    count = 1
    while slow != fast:
        slow, fast = slow.next, fast.next.next
        count += 1
    cur1 = headA
    # find the intersection
    while count != 0:
        cur1 = cur1.next
        count -= 1
    cur2 = headA
    while cur1 != cur2:
        cur1, cur2 = cur1.next, cur2.next
    return cur1

def getIntersectionNode1( headA, headB):
    arr1, arr2 = [], []
    cur1, cur2 = headA, headB
    while cur1:
        arr1.append(cur1.val)
        cur1 = cur1.next
    while cur2:
        arr2.append(cur2.val)
        cur2 = cur2.next

    n1, n2 = len(arr1), len(arr2)
    count = 0
    while len(arr1) and len(arr2) and arr1.pop() == arr2.pop():
        count += 1
    if count == 0:
        return None
    else:
        position = n1 - count + 1
        cur, count = headA, 0
        while count != position:
            count += 1
            cur = cur.next
        return cur


if __name__ == '__main__':
    head1 = L.ListNode().produce([4,1,8,4,5])
    head2 = L.ListNode().produce([5,6,1,8,4,5])
    ans = getIntersectionNode(head1, head2)