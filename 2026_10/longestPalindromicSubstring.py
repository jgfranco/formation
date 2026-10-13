

"""
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/description/

Solved
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(i,j):
            left= i
            right = j

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -=1
                right +=1

            return left+1, right-1

        longest = ""
        for i in range(len(s)):
            #odd
            left, right = expand(i,i)
            
            if len(longest) < (right -left) + 1:
                print(left, right)
                longest = s[left:right+1]
                print(longest)
            #even
            left, right = expand(i, i+1)
            if len(longest) < (right -left) + 1:
                longest = s[left:right+1]
        
        return longest