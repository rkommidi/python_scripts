# input : AAAAAAAAAAAAABBCCCCDD  output: 9A4A2B4C2D
#O(n) time | O(n) space

def runLengthEncoding(string):
    encoded_chars = []
	run_length = 1
	for i in range(1,len(string)+1):
		if i == len(string) or run_length == 9 or string[i] != string[i-1] :
			encoded_chars.append(str(run_length))
			encoded_chars.append(string[i-1])
			run_length = 1
		else:
			run_length += 1
			
	return "".join(encoded_chars)
