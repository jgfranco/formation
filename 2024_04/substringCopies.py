
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
Time: O() 
Space: O()
 

📆 PLAN
Outline of algorithm #: 



🛠️ IMPLEMENT
function strCopies(word, sub, n) {
def strCopies(word: str, sub: str, n: int) -> bool: 
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def strCopies(word, sub, n, index = 0):
  if len(word)- index < len(sub):
    if n == 0:
      return True
    return False

  if word.startswith(sub, index):
    n -=1
  
  return strCopies(word, sub, n, index +1)


assert strCopies("catcowcat", "cat", 2) == True
assert strCopies("catcowcat", "cow", 2) == False
assert strCopies("catcowcat", "cow", 1) == True
assert strCopies("catcowcatcat", "cat", 2) == False
assert strCopies("ccatcowcatcat", "cat", 3) == True
