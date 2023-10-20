class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def constructOptimalBST(keys, opt, i, j):
    if i > j:
        return None

    root_index = opt[i][j]
    root = TreeNode(keys[root_index])

    root.left = constructOptimalBST(keys, opt, i, root_index - 1)
    root.right = constructOptimalBST(keys, opt, root_index + 1, j)

    return root

def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.key)
        printInorder(root.right)
