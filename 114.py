import TreeNode as TN


def hasPathSum(root):
    root = DFS(root)


def DFS(root):
    if root == None:
        return
    treeNode = TN.TreeNode(root.val)
    treeNode.left = None
    treeNode.right = DFS(root.left)
    cur = treeNode
    while cur.right:
        cur = cur.right
    cur.right = DFS(root.right)
    return treeNode

if __name__ == '__main__':
    root = TN.TreeNode(1)
    root.left = TN.TreeNode(2)
    root.left.left = TN.TreeNode(3)
    root.left.right = TN.TreeNode(4)
    root.right = TN.TreeNode(5)
    root.right.right = TN.TreeNode(6)
    ans = hasPathSum(root)