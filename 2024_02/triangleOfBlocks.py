
'''
❓ PROMPT
We have a triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks, the next row has 3 blocks, and so on. Compute recursively (no loops or multiplication) the total number of blocks in such a triangle with the given number of rows.

Example(s)
triangle(2) == 3
triangle(3) == 6
triangle(5) == 15


        _
       _ _
      _ _ _
     _ _ _ _
    _ _ _ _ _
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: recursion, base case is number of rows is 0, return 0
Time: O(n) where n is the number of rows
Space: O(n) where n represents the call stack
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function triangle(rows) {
def triangle(rows: int) -> int:

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

def triangle(rows):
  if rows < 0: return -1

  if rows == 0: return 0

  return rows + triangle(rows-1)


print(triangle(2))
print(triangle(3))
print(triangle(5))
print(triangle(6))


print(triangle(12) == 78)
print(triangle(7) == 28)
print(triangle(6) == 21)
print(triangle(5) == 15)
print(triangle(4) == 10)
print(triangle(3) == 6)
print(triangle(2) == 3)
print(triangle(1) == 1)
print(triangle(0) == 0)