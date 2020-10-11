
# O(n) time and O(1) space
def isValidSubsequence(array, sequence):
    # Write your code here.
	seqIdx = 0
	for val in array:
		if seqIdx == len(sequence):
			break
		if sequence[seqIdx] == val:
			seqIdx += 1

	return seqIdx == len(sequence)
