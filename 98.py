import TreeNode as TreeNode


def isValidBST(root: TreeNode) -> bool:
    return DFS(root, float('inf'), float('-inf'))


def DFS(root, maxValue, minValue):
    if root == None:
        return True
    if root.val <= minValue or root.val >= maxValue:
        return False
    return DFS(root.left, minValue, root.val) and DFS(root.right, root.val, maxValue)

if __name__ == '__main__':
    root = TreeNode.TreeNode(2)
    root.left = TreeNode.TreeNode(1)
    root.right = TreeNode.TreeNode(3)
    ans = isValidBST(root)