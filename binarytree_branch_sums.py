
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(n) space - where n is the number of nodes in the Binary Tree
def branchSums(root):
	sums = []
    calculateBranhSums(root, 0, sums)
	return sums


def calculateBranhSums(node, runningSum, sums):
	if node is None:
		return

	newRunningSum = runningSum + node.value
	if node.left is None and node.right is None:
		sums.append(newRunningSum)
		return

	calculateBranhSums(node.left,newRunningSum,sums)
	calculateBranhSums(node.right,newRunningSum,sums)
