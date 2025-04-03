"""
https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0 
        right = len(height) - 1

        maxArea = 0

        while left < right:
            leftHeight = height[left]
            rightHeight = height[right]

            width = right - left
            minHeight = min(leftHeight, rightHeight)
            area = width * minHeight
            maxArea = max(maxArea, area)

            if leftHeight < rightHeight:
                left +=1
            else:
                right -=1
        
        return maxArea


        