"""
https://leetcode.com/problems/guess-number-higher-or-lower/description/?envType=study-plan-v2&envId=leetcode-75
"""


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# 


class Solution:
    def __init__(self, pick: int):
        self.pick = pick

    def guess(self, num: int) -> int:
        if num == self.pick: return 0
        elif num > self.pick: return -1
        else: return 1

    def guessNumber(self, n: int) -> int:
        
        left = 1
        right = n 
        
        while left <= right:
            mid = (right + left) // 2
            result = self.guess(mid)

            if result == 0:
                return mid
            elif result == 1:
                left = mid + 1
            else:
                right = mid -1

        