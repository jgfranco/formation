"""
https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1 = p2 = 0
        l1 = len(word1)
        l2 = len(word2)
        merged = []
        while p1 < l1 or p2 < l2:
            if p1 < l1:
                merged.append(word1[p1])
                p1 +=1
            if p2 < l2:
                merged.append(word2[p2])
                p2 +=1

        return "".join(merged)

