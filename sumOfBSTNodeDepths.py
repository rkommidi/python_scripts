
#O(n) and O(h)
def nodeDepths(root):
    # Write your code here.
	sumOfDepths = 0
	stack = [{"node":root,"depth":0}]
	while len(stack) > 0:
		nodeInfo = stack.pop()
		node, depth = nodeInfo["node"], nodeInfo["depth"]
		sumOfDepths += depth
		if node.left is not None:
			stack.append({"node": node.left, "depth": depth + 1 })
		if node.right is not None:
			stack.append({"node": node.right, "depth": depth + 1 })

	return sumOfDepths



# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
