"""
https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:

        p = 0

        leftSum = 0
        rightSum = sum(nums) - nums[0]

        while p< len(nums):

            if leftSum == rightSum:
                return p
            
            leftSum += nums[p]
            p += 1
            if p < len(nums):
                rightSum  -= nums[p]
            
        return -1

