'''
❓ PROMPT
Given a string, recursively compute a new string where identical chars that are adjacent in the original string are separated from each other by a "*".

Example(s)
pairStars("hello") == "hel*lo"
pairStars("xxyy") == "x*xy*y"
pairStars("aaaa") == "a*a*a*a" 

🔎 EXPLORE
List your assumptions & discoveries:

Insightful & revealing test cases: 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O(n) where n represents the length of the string
Space: O(n) if we consider the stack, we are going to have a call per char
 
📆 PLAN
Outline of algorithm #: 
  base case: if the length of the string is less than 1, return the word as is

  compare the first two characters of the word at index 0 and 1
  if they are the same add an astersik between the first character and the recursive call on the rest of the string
  otherwise, return the character followed by the recursive call on the rest of the string

🛠️ IMPLEMENT
function pairStars(word) {
def pairStars(word: str) -> str:
'''
def pairStars(word):
  
  if len(word) <= 1: return word

  if word[0] == word[1]:
    return word[0] + "*" + pairStars(word[1:])
  return word[0] + pairStars(word[1:])
'''
 
🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
print(pairStars("hello") == "hel*lo")
print(pairStars("xxyy") == "x*xy*y")
print(pairStars("aaaa") == "a*a*a*a")
print(pairStars("aaab") == "a*a*ab")
print(pairStars("aa") == "a*a")
print(pairStars("a") == "a")
print(pairStars("") == "")
print(pairStars("noadjacent") == "noadjacent")
print(pairStars("abba") == "ab*ba")
print(pairStars("abbba") == "ab*b*ba")