def findThreeLargestNumbers(array):
	result = []
    for item in array:
		if len(result) == 3:
			if item > result[0]:
				del result[0]
				result.append(item)				
		else:	
			result.append(item)
		
		result.sort()
		print(result)

	return result
