"""
https://leetcode.com/problems/max-consecutive-ones-iii/description/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        
        #     l 
        # 11100011110
        #           r     
        
        motherFlippinZeroes = 0
        left = right = 0
        res = 0
        
        while right < len(nums):
            
            r = nums[right]
            
            if r == 0:
                motherFlippinZeroes +=1
                
            while motherFlippinZeroes == k+1:
                l = nums[left]
                if l == 0:
                    motherFlippinZeroes -=1
                left += 1
                
            res = max(res, right-left +1)
            right += 1
            
        return res