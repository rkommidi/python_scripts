# function that takes in a non-empty array of intergers that are sorted in ascending order and returns a new array of the same length with the squares of the original integers also sorted in ascending order

# array = [-7, -3, 1,9,22,30]
# output
# [ 1,9,49,81,484,900]

# O(n) time | O(n) space - where n is the length of the input array
def sortedSquareArray(array):
    sortedSquares = [0 for _ in array]
    smallerValueIdx = 0
    largerValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue * largerValue
            largerValueIdx -= 1

    return sortedSquares
