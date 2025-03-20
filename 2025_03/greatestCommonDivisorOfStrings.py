"""
https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75"

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

"""

class Solution:
    def gcd(self, x: int, y: int) -> int:
        if y == 0:
            return x
        else:
            return self.gcd(y, x % y)
        
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return None
        
        max_length = self.gcd(len(str1), len(str2))
        return str1[:max_length]


print(Solution().gcdOfStrings("ABCABC", "ABC")) # "ABC"
print(Solution().gcdOfStrings("ABABAB", "ABAB")) # "AB"
print(Solution().gcdOfStrings("LEET", "CODE")) # None
print(Solution().gcdOfStrings("ABABAB", "AB")) # AB