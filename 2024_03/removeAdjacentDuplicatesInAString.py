"""
1047. Remove All Adjacent Duplicates In String
Easy

6446

244

Add to List

Share
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""
class Solution:
  def removeDuplicates(self, s: str) -> str:

    '''
    🔎 EXPLORE
    What are some other insightful & revealing test cases?
    


    🧠 BRAINSTORM
    What approaches could work? 
    Algorithm 1: use a stack

    Time: O(N)
    Space: O(N)
    

    📆 PLAN
    Outline of algorithm #: 
    

    🛠️ IMPLEMENT
    Write your algorithm.
    '''
    stack = []
    
    for char in s:
        if stack and char == stack[-1]:
            stack.pop()
            continue
        stack.append(char)

    return "".join(stack)
  
    '''

    🧪 VERIFY
    Run tests. Methodically debug & analyze issues.

    '''