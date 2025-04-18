"""
https://leetcode.com/problems/unique-number-of-occurrences/description/?source=submission-ac
"""

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        from collections import defaultdict
        counts = defaultdict(int)
        visited = set()

        for num in arr:
            counts[num] += 1

        for count in counts.values():
            if count in visited: return False
            visited.add(count)

        return True