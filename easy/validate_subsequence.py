#!/usr/bin/env python3
# given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.

# array = [ 5,1,22,25,6,-1,8,10]
# seq = [1,6,-1,10]

#output
# true

# O(n) time and O(1) space
def isValidSubsequence(array, sequence):
	seqIdx = 0
	for val in array:
		if seqIdx == len(sequence):
			break
		if sequence[seqIdx] == val:
			seqIdx += 1

	return seqIdx == len(sequence)

def test_isvalid():
    assert isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]) == True, "Should be True"
    assert isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [4, 5, 1, 22, 25, 6, -1, 8, 10]) == False, "Should be False"

if __name__ == "__main__":
    test_isvalid()
    print("Everything passed")
