from TreeNode import TreeNode


def recoverTree( root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    arr = []
    DFS(root, arr)
    first, second = None, None
    for i in range(len(arr) - 1):
        if arr[i].val > arr[i+1].val and not first:
            first = arr[i]
        if arr[i].val > arr[i+1].val and first:
            second = arr[i+1]
    first.val, second.val = second.val, first.val



def DFS( root, ans):
    if root:
        DFS(root.left, ans)
        ans.append(root)
        DFS(root.right, ans)

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)
    ans = recoverTree(root)