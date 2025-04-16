"""
https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        
        nums1Set = set(nums1)
        nums2Set = set(nums2)

        notInNums2 = set()
        notInNums1 = set()

        for num in nums1Set:
            if num not in nums2Set:
                notInNums2.add(num)
        
        for num in nums2Set:
            if num not in nums1Set:
                notInNums1.add(num)

        return [list(notInNums2), list(notInNums1)]