"""
https://leetcode.com/problems/decode-string/?envType=study-plan-v2&envId=leetcode-75
"""

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        number = 0
        output = ""

        for char in s:
            if char.isdigit():
                number = number * 10 + int(char) 
            elif char == "[":
                stack.append(number) 
                stack.append(output)
                number = 0
                output = ""
            elif char == "]":
                prevString = stack.pop() 
                prevNumber = stack.pop() 
                output = prevString + output * prevNumber
            else: 
                output += char

        return output
