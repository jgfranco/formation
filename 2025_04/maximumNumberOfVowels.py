"""
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        if k > len(s): return 0

        vowels = {'a','e','i','o','u'}

        start = 0
        end = k - 1
        vowelCount = 0
        maxVowels = float('-inf')

        while end < len(s):
            if start == 0:
                for char in s[start:end + 1]:
                    if char in vowels:
                        vowelCount += 1
            else:
                if s[start -1] in vowels:
                    vowelCount -=1
                if s[end] in vowels:
                    vowelCount += 1
            
            start += 1
            end += 1
            if vowelCount > maxVowels:
                maxVowels = vowelCount

        
        return maxVowels
        