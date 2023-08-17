'''
https://leetcode.com/problems/remove-outermost-parentheses/

1021. Remove Outermost Parentheses
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

 

Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: s = "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
 
🔎 EXPLORE
What are some other insightful & revealing test cases?
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: 
use a stack
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 

 
'''
'''
🛠️ IMPLEMENT
Write your algorithm.
'''                                      
def removeOutermostParentheses(string): 
    counter = 0 

    result = [] 

    for char in string:
      if char ==")":
        counter -=1
      if counter >0:
        result.append(char)
      if char == "(":
        counter +=1

    return "".join(result)
          
    
'''

1210
(())
1010
()()

🧪 VERIFY
Run tests. Methodically debug & analyze issues.
'''

print(removeOutermostParentheses("()()"), 'expect empty string')
print(removeOutermostParentheses("(()())"), 'expect ()()')
print(removeOutermostParentheses("(())"), 'expect ()')
