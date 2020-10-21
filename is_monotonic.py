
#An array is said to be monotonic if its elements, from left to right, are entirely non-increasing or entirely non-decreasing
#Note that empty arrays and arrays of one element are monotonic

#O(n) time | O(1) space
def isMonotonic(array):
	isNonDecreasing = True
	isNonIncreasing = True
	for i in range(1,len(array)):
		if array[i] < array[i-1]:
			isNonDecreasing = False
		if array[i] > array[i-1]:
			isNonIncreasing = False

	return isNonDecreasing or isNonIncreasing

