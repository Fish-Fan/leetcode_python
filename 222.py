import TreeNode as T


def countNodes(root):
    global count
    count = 0
    counthelper(root)
    return count

def counthelper(root):
    if root:
        global count
        count += 1
        counthelper(root.left)
        counthelper(root.right)


if __name__ == '__main__':
    root = T.TreeNode(1)
    root.left = T.TreeNode(2)
    root.right = T.TreeNode(3)
    root.left.left = T.TreeNode(4)
    root.left.right = T.TreeNode(5)
    root.right.left = T.TreeNode(6)
    ans = countNodes(root)
    print(ans)

