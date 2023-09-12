
'''
https://leetcode.com/problems/backspace-string-compare/

844. Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
🔎 EXPLORE
What are some other insightful & revealing test cases?
 

🧠 BRAINSTORM
What approaches could work? use a stack so I can pop the last element whenever a hashtag is found. 
pass both strings throug this helper method and compare them at the end
Algorithm 1:
Time: O(n+m) where n represents the length of string 1 and m represents the lenght of string 2
Space: O(n+m)
 

📆 PLAN
Outline of algorithm #: 
use a helper method
  traverse the string, appending each character to an array
  whenever the hashtag symbol is found, pop the last character in the array

call this function for both strings, compare strings at the end, return True if equal, False otherwise
 

🛠️ IMPLEMENT
Write your algorithm.
'''
def backspaceCompare(string1, string2):
  def helper(string):
    chars = []

    for char in string:
      if char == "#" :
        if len(chars) != 0: chars.pop()
      else:
        chars.append(char)
    return "".join(chars)
  
  return helper(string1)== helper(string2)

'''
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

print(backspaceCompare("ab#c", "ad#c"), True)
print(backspaceCompare("a#c", "c"), True)
print(backspaceCompare("", "ad#c"), False)
print(backspaceCompare("#c", "c"), True)
print(backspaceCompare("a#c", "b"), False)
print(backspaceCompare("ab##", "c#d#"), True)
print(backspaceCompare("", "cd##"), True)
