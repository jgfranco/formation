"""
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        
        zeroCount = 0
        longestWindow = 0

        start = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
            
            while zeroCount > 1:
                if nums[start] == 0:
                    zeroCount -= 1
                start += 1
            
            longestWindow = max(longestWindow, i - start)
            print(longestWindow)
        
        return longestWindow