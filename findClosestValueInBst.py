#O(n) time and O(1) space
def findClosestValueInBst(tree, target):
    # Write your code here.
	closest = tree.value
    while tree is not None:
		diff = target - tree.value
		if abs(target - closest) > abs(target - tree.value):
			closest = tree.value
		if diff == 0:
			return tree.value
		elif diff < 0:
			tree = tree.left
		elif diff > 0:
			tree = tree.right
	return closest
		


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
