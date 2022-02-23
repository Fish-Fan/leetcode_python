import ListNode as L
import TreeNode as T

def sortedListToBST(head):
    global cur

    cur = head
    tmp = head
    n = 0
    while tmp:
        n += 1
        tmp = tmp.next
    return helper(n)


def helper(n):
    if n <= 0:
        return None
    global cur
    left = helper(n//2)
    root = T.TreeNode(cur.val)
    root.left = left
    cur = cur.next
    right = helper(n-n//2-1)
    root.right = right
    return root


if __name__ == '__main__':
    listNode = L.ListNode()
    head = listNode.produce([1,2,3,4,5,6,7,8,9])
    ans = sortedListToBST(head)