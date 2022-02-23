import TreeNode as TN


def sumNumbers(root) -> int:
    ans = []
    DFS(root, 0, ans)
    return sum(ans)


def DFS(root, path, ans):
    path = path * 10 + root.val
    if root and root.left == None and root.right == None:
        ans.append(path)
        return
    DFS(root.left, path, ans)
    DFS(root.right, path, ans)

if __name__ == '__main__':
    root = TN.TreeNode(1)
    root.left = TN.TreeNode(2)
    root.right = TN.TreeNode(3)
    sumNumbers(root)