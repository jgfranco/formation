
'''
❓ PROMPT
Given an org chart of a company, employee A, and employee B: 
figure out if employee B is a direct report to employee A.

Employee B must report directly to employee A - this occurs 
if Employee A is the parent node of Employee B.

Employees in our tree are represented as integer values (eg: 1).

Return true if employee A manages employee B, false if not.

Example(s)
      1  <---- ceo
     / \
    2   3
       / \
      4   5
     /
    6  
isDirectReport(ceo, 1, 2) == True
isDirectReport(ceo, 1, 4) == False
isDirectReport(ceo, 2, 1) == False
isDirectReport(ceo, 2, 3) == False
isDirectReport(ceo, 3, 4) == True
 

🔎 EXPLORE
List your assumptions & discoveries:
employee B must be employee's A child 
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
find employee A (via BFS) and if employee B is part of its children return True, otherwise return False
Algorithm 1:
Time: O(n)
Space: O(n)

 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
function isDirectReport(person, manager, employee) {
'''
class Node:
  def __init__(self, value, left = None, right = None) -> None:
    self.value = value
    self.left = left
    self.right = right

def isDirectReport(person: Node, manager: int, employee: int) -> bool:
  if not person: return False
  
  from collections import deque
  q = deque([person]) 

  while q:
    node = q.popleft()

    if node.value == manager:
      if node.left and node.left.value == employee: return True
      elif node.right and  node.right.value == employee: return True
      else: return False
    
    if node.left:
      q.append(node.left)
    if node.right:
      q.append(node.right)
  
  return False

'''
🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

#     1
#   2   3
#      4  5
#     6  
ceo = Node(1,
        Node(2),
        Node(3,
          Node(4,
            Node(6)),
          Node(5)
      ))

# 5
solo = Node(5)

#   5
# 10
partner = Node(5,
            Node(10)
          )

print(isDirectReport(None, 1, 2) == False)
print(isDirectReport(solo, 1, 2) == False)
print(isDirectReport(partner, 5, 5) == False)
print(isDirectReport(partner, 5, 10) == True)
print(isDirectReport(ceo, 1, 2) == True)
print(isDirectReport(ceo, 1, 4) == False)
print(isDirectReport(ceo, 2, 1) == False)
print(isDirectReport(ceo, 2, 3) == False)
print(isDirectReport(ceo, 3, 1) == False)
print(isDirectReport(ceo, 3, 5) == True)
print(isDirectReport(ceo, 4, 5) == False)
print(isDirectReport(ceo, 4, 6) == True)
print(isDirectReport(ceo, 1, 1) == False)
print(isDirectReport(ceo, 4, 4) == False)
