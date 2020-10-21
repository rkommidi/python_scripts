
def smallestDifference(arrayOne, arrayTwo):
	arrayOne.sort()
	arrayTwo.sort()
	closest = float("inf")

	firstIdx = 0
	secondIdx = 0

	result = []
	while firstIdx < len(arrayOne) and secondIdx < len(arrayTwo):
		firstNum = arrayOne[firstIdx]
		secondNum = arrayTwo[secondIdx]
		if firstNum < secondNum:
			current = secondNum - firstNum
			firstIdx += 1
		elif secondNum < firstNum:
			current = firstNum - secondNum
			secondIdx += 1
		else:
			return [firstNum, secondNum]

		if closest > current:
			closest = current
			result = [firstNum, secondNum]


	return result

