"""
https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "": return True
        
        p = 0
        for char in t:
            if p < len(s) and s[p] == char:
                p+=1
        
        return p == len(s)