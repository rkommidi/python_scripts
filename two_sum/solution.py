#!/usr/bin/env python3

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for pos, i in enumerate(nums):
            complement = target - nums[pos]
            if ( complement in checked ):
                return [checked[complement], pos]
            
            checked[nums[pos]] = pos
            
            
def main():
    sol = Solution()
    result = sol.twoSum([2,7,11,15],9)
    print(result)
    
    
if __name__ == "__main__":
    main()
