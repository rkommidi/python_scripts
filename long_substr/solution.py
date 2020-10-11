#!/usr/bin/env python3

class Solution:
    def lengthOfLongestSubstring(self, s):
        dicts = {}
        maxlength = start = 0
        for i,value in enumerate(s):
            if value in dicts:
                sums = dicts[value] + 1
                if sums > start:
                    start = sums
            num = i - start + 1
            if num > maxlength:
                maxlength = num
            dicts[value] = i
        return maxlength

def main():
    sol = Solution()
    result = sol.lengthOfLongestSubstring("abcbaef")
    print(result)
    
    
if __name__ == "__main__":
    main()
