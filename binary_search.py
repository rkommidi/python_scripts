
# O(log(n)) time | O(1) space
def binarySearch(array, target):
    left = 0
    right = len(array) -1
    while left <= right:
        middle = (left + right ) // 2
        if array[middle] > target:
	    right = middle - 1
	elif array[middle] < target:
	    left = middle + 1
        else:
            return middle
    return -1
