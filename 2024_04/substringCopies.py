
'''
❓ PROMPT
Given a string and a non-empty substring *sub*, compute recursively if at least n 
copies of sub appear in the string somewhere, possibly with overlapping. N will be non-negative.

Example(s)
strCopies("catcowcat", "cat", 2) == True
strCopies("catcowcat", "cow", 2) == False
strCopies("catcowcat", "cow", 1) == True
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work? use slice to compare word vs substring 
Algorithm 1:
Time: O(N) where N is the length of the word. Worst case scenario we would be slicing the word one character at a time
Space: O(N) where N is the size of the callstack
 

📆 PLAN
Outline of algorithm #: 
base case 1: if the word is empty and the counter is 0, return True
base case 2: if the word is empty return False

slice the word  from the beginning to the size of the subString
if they are the same: call recursively on the rest of the word, decrement the counter (n)
otherwise, slice the word by one (remove the first character) and call recursively 


🛠️ IMPLEMENT
function strCopies(word, sub, n) {
def strCopies(word: str, sub: str, n: int) -> bool: 
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def strCopies(word, sub, n):
  if n == 0 and word == "":
    return True
  if word == "":
    return False
  
  subSize = len(sub)

  if sub == word[:subSize]:
    return strCopies(word[subSize:], sub, n-1)
  
  return strCopies(word[1:], sub, n)


assert strCopies("catcowcat", "cat", 2) == True
assert strCopies("catcowcat", "cow", 2) == False
assert strCopies("catcowcat", "cow", 1) == True
assert strCopies("catcowcatcat", "cat", 2) == False
assert strCopies("ccatcowcatcat", "cat", 3) == True
