#O(nlogn) time O(1) time
def twoNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
	
    return []


def main():
    result = twoNumberSum([2,7,11,15],9)
    print(result)
    
    
if __name__ == "__main__":
    main()
