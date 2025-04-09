"""
https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75
"""
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        p = 0
    
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[p], nums[r] = nums[r], nums[p]
                p += 1
            
        return nums