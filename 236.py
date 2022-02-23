import TreeNode as TN


def lowestCommonAncestor(root, p, q):
    preorder = []
    postorder = []
    d = {}
    preorderTravel(root, preorder, d)
    postorderTravel(root, postorder)
    preDict, postDict = {}, {}
    for i, v in enumerate(preorder):
        preDict[v] = i
    for i, v in enumerate(postorder):
        postDict[v] = i
    left, right = 0, len(preorder)
    ans = []
    exist(left, right, root.val, preorder, postorder, ans, preDict, postDict, p, q)
    return d.get(ans[-1])

def exist( left, right, root, preorder, postorder, ans, preDict, postDict, p, q):
    if preDict.get(p.val) > left and preDict.get(q.val) > left and preDict.get(p.val) < right and preDict.get(
            q.val) < right:
        ans.append(root)
        rightIdx = preDict.get(postorder[postDict.get(root) + 1])
        exist(preDict.get(root) + 1, rightIdx, preorder[preDict.get(root) + 1], preorder, postorder, ans,
                   preDict, postDict, p, q)
        exist(rightIdx, len(preorder), preorder[rightIdx], preorder, postorder, ans, preDict, postDict, p, q)

def preorderTravel( node, preorder, d):
    if node:
        d[node.val] = node
        preorder.append(node.val)
        preorderTravel(node.left, preorder, d)
        preorderTravel(node.right, preorder, d)

def postorderTravel( node, postorder):
    if node:
        postorder.append(node.val)
        postorderTravel(node.right, postorder)
        postorderTravel(node.left, postorder)


if __name__ == '__main__':
    root = TN.TreeNode(3)
    root.left = TN.TreeNode(5)
    root.left.left = TN.TreeNode(6)
    root.left.right = TN.TreeNode(2)
    root.left.right.left = TN.TreeNode(7)
    root.left.right.right = TN.TreeNode(4)
    root.right = TN.TreeNode(1)
    root.right.left = TN.TreeNode(0)
    root.right.right = TN.TreeNode(8)

    p = root.left.right.left
    q = root.left.right.right
    ans = lowestCommonAncestor(root, p, q)