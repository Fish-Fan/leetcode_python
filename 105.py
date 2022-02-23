class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



if __name__ == '__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    print(node)