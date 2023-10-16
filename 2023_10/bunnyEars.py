
'''
❓ PROMPT
We have a number of bunnies, each with two big floppy ears. 
We want to compute the total number of ears across all the bunnies recursively, 
without loops or multiplication.

Example(s)
bunnyEars(3) == 6
bunnyEars(5) == 10
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
recursive function:
  base case, the number of bunnies is zero in which case the number of ears is 0 (return 0)

  otherwise return 2 and add the result of the recursive call on bunnies - 1
Time: O(n) where n is the number of bunnies
Space: O(n) if we consider the call stack
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function bunnyEars(bunnies) {
'''
def bunnyEars(bunnies: int) -> int:
  if bunnies ==0: return 0

  return 2 + bunnyEars(bunnies-1)

'''

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

print(bunnyEars(3) == 6)
print(bunnyEars(5) == 10)
print(bunnyEars(7) == 14)
print(bunnyEars(4) == 8)
print(bunnyEars(2) == 4)
print(bunnyEars(1) == 2)
print(bunnyEars(0) == 0)