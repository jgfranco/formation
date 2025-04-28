"""
https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution:
    
    def equalPairs(self, grid: list[list[int]]) -> int:
        from collections import defaultdict
        m = defaultdict(int)
        count = 0
        for row in grid:
            m[str(row)] +=1

        for c in range(len(grid[0])):
            colNums = []
            for r in range(len(grid)):
                colNums.append(grid[r][c])
            
            count += m[str(colNums)]

        return count

