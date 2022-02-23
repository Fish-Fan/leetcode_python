import TreeNode as TN


def lowestCommonAncestor(root, p, q):
    ans = ''
    DFS(root, p, q, ans)
    return ans


def DFS(node, p, q, ans):
    d = {}
    travel(node, d)
    if p in d and q in d:
        ans = node
        DFS(node.left, p, q, ans)
        DFS(node.right, p, q, ans)


def travel( node, d):
    if node:
        d[node.val] = 1
        travel(node.left, d)
        travel(node.right, d)

if __name__ == '__main__':
    root = TN.TreeNode(6)
    root.left = TN.TreeNode(2)
    root.left.left = TN.TreeNode(0)
    root.left.right = TN.TreeNode(4)
    root.right = TN.TreeNode(8)
    root.right.left = TN.TreeNode(7)
    root.right.right = TN.TreeNode(9)
    root.left.right.right = TN.TreeNode(5)
    root.left.right.left = TN.TreeNode(3)

    ans = lowestCommonAncestor(root, 5, 9)