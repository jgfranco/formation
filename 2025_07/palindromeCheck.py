
"""
Problem Prompt
Your task is to determine if a given string is a palindrome. A palindrome is a sequence that reads the same backward as forward. For this problem, consider only alphanumeric characters and ignore cases. An empty string is considered a valid palindrome.
Example(s)
Example 1:
Input: 'A man, a plan, a canal: Panama'
Output: true

Example 2:
Input: 'race a car'
Output: false
Signature/Prototype
function isPalindrome(s: string): boolean
Expand these sections to compare against our recommendations.

"""

def isPalindrome(s):

    s = s.lower()

    l = 0
    r = len(s) - 1
    
    while l < r:
        while not s[l].isalnum():
            l += 1

        while not s[r].isalnum():
            r -= 1

        if s[l] != s[r]:
            return False

        l += 1
        r -= 1

    return True



print(isPalindrome('A man, a plan, a canal: Panama') == True)
print(isPalindrome('race a car') == False)
print(isPalindrome(' ') == True)
print(isPalindrome('0P') == False)

print(isPalindrome("A") == True)
print(isPalindrome("AA") == True)