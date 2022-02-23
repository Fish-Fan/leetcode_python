import TreeNode as TN


def hasPathSum(root, targetSum: int) -> bool:
    return DFS(root, targetSum)


def DFS(root, target):
    if target == 0:
        return True
    elif target < 0:
        return False

    if root.left and root.right:
        return DFS(root.left, target - root.val) or (root.right, target - root.val)
    elif root.right:
        return DFS(root.right, target - root.val)
    elif root.left:
        return DFS(root.left, target - root.val)
    else:
        return False

if __name__ == '__main__':
    root = TN.TreeNode(5)
    root.left = TN.TreeNode(4)
    root.left.left = TN.TreeNode(11)
    root.left.left.left = TN.TreeNode(7)
    root.left.left.right = TN.TreeNode(2)
    root.right = TN.TreeNode(8)
    root.right.left = TN.TreeNode(13)
    root.right.right = TN.TreeNode(4)
    root.right.right.right = TN.TreeNode(1)
    ans = hasPathSum(root, 22)