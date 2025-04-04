"""
https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75

You are given an integer array nums and an integer k.
You can perform the following operation as many times as you want:
Choose two integers in nums such that they sum up to k and remove them from nums.
Return the maximum number of operations you can perform on nums.
Example 1: 
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation:
1 + 4 = 5, remove 1 and 4 from nums.
2 + 3 = 5, remove 2 and 3 from nums.
"""


class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        if len(nums) < 2: return 0

        nums.sort()

        left = 0
        right= len(nums) -1
        operations  = 0

        while left < right:

            if nums[left] + nums[right] ==k:
                operations += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] > k:
                right -=1
            else:
                left += 1
        
        return operations