
# Function that takes in a non-empty of distinct integers and an integer representing a target sum. if any two numbers in the input array sum up to the target sum, the funtion should return them in an array, in any order. if no two numbers dum up to the target sum, the function should return an empty array.
# array = [ 3,5,-4,8,11,1,-1,6]
# targetSum = 10

#output
# [-1, 11] // the numbers could be in reverse order
def twoNumberSum(array, targetSum):
	checked = {}
	for i in array:
		complement = targetSum - i
		if complement in checked:
			return [i, complement]
		else:
			checked[i] = 1

	return []
