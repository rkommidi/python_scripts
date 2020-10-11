#!/usr/bin/env python3

class Solution(object):
    def compress(self, chars):
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write

def main():
    sol = Solution()
    input_string = input("Enter String for Compression:")
    chars = [ ele for ele in input_string ]
    result = sol.compress(chars)
    print(chars)
    print(chars[0:result])
    print(result)
    
    
if __name__ == "__main__":
    main()
