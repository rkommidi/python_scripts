#!/usr/bin/env python3

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hm = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }
        out = []
        possible = []
        for d in digits:
            possible.append(hm[d])

        self.dfs(0, '', out, possible)
        return out

    def dfs(self, index, current, out, possible):
        print(index)
        print(current)
        if len(current) == len(possible):
            if current != "":
                out.append(current)
            return
        for i in possible[index]:
            self.dfs(index+1, current+i, out, possible)


def main():
    number = input("Enter Number:")
    print(number)
    sol = Solution()
    result = sol.letterCombinations(number)
    print(result)


if __name__ == "__main__":
    main()
