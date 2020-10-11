
def twoNumberSum(array, targetSum):
	checked = {}
	for i in array:
		complement = targetSum - i
		if complement in checked:
			return [i, complement]
		else:
			checked[i] = 1

	return []


def main():
    result = twoNumberSum([2,7,11,15],9)
    print(result)
    
    
if __name__ == "__main__":
    main()

