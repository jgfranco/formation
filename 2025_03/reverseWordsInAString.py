"""
https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75

Given an input string s, reverse the order of the words.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split(" ")

        result = []
        for word in words:

            if word != "":
                result.append(word)

        return " ".join(result[::-1])
    
print(Solution().reverseWords("the sky is blue")) # "blue is sky the"
print(Solution().reverseWords("  hello world  ")) # "world hello"
print(Solution().reverseWords("a good   example")) # "example good a"
print(Solution().reverseWords("  Bob    Loves  Alice   ")) # "Alice Loves Bob"