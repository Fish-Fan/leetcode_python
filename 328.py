import ListNode as LN
def oddEvenList(head):
    oddHead, evenHead = LN.ListNode(0), LN.ListNode(0)
    cur, count = head, 0
    oddCur, evenCur = oddHead, evenHead
    while cur:
        count += 1
        if count % 2 == 1:
            oddCur.next = cur
            oddCur = oddCur.next
        else:
            evenCur.next = cur
            evenCur = evenCur.next
        cur = cur.next

    oddCur.next = evenHead.next
    if count % 2 == 1:
        evenCur.next = None
    return oddHead.next
if __name__ == '__main__':
    ls = LN.ListNode()
    arr = [1,2,3,4,5]
    head = ls.produce(arr)
    ans = oddEvenList(head)
    print(ans)
