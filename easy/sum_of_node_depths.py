#Sum of BST nodes depth

def nodeDepths(root):
    depthSums = [0]
    nodeDepthHelper(root,0, depthSums)
    return depthSums[0]

def nodeDepthHelper(node, depth, depthSums):
    if node is None:
        return
    depthSums[0] += depth
    nodeDepthHelper(node.left, depth+1, depthSums)
    nodeDepthHelper(node.right, depth+1, depthSums)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

