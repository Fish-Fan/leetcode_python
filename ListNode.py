class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def produce(self, arr):
        head = ListNode(None)
        current = head
        for v in arr:
            current.next = ListNode(v)
            current = current.next
        return head.next

    def producewithcycle(self, arr, pos):
        head = self.produce(arr)
        tail = head
        while tail.next:
            tail = tail.next
        count = 0
        tmp = head
        while count != pos:
            count += 1
            tmp = tmp.next
        tail.next = tmp
        return head
