

"""
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        """
        first intuition is to do a pass and get the number of candies that the kid with the most has (get the max)
        """
        results = []
        maxCandies = max(candies)
        for num in candies:
            if num + extraCandies >= maxCandies:
                results.append(True)
            else:
                results.append(False)
        
        return results
    

print(Solution().kidsWithCandies([2,3,5,1,3], 3)) # [True, True, True, False, True]
print(Solution().kidsWithCandies([4,2,1,1,2], 1)) # [True, False, False, False, False]
print(Solution().kidsWithCandies([12,1,12], 10)) # [True, False, True]
