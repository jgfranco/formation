"""
https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:

        highest = 0
        altitude = 0

        for g in gain:
            altitude = g + altitude
            if altitude > highest:
                highest = altitude
        
        return highest

        