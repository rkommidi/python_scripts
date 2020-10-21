
#O(n) time | O(1) space - where n is the length of the array
def moveElementToEnd(array, toMove):

	rIdx = 0
	for pos,element in enumerate(array):
		if element != toMove:
			array[rIdx], array[pos] = array[pos], array[rIdx]
			rIdx += 1
	return array
