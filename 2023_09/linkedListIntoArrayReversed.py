'''
❓ PROMPT
Given a linked list, return an array with all the elements in reverse.

Example(s)
head = 1 -> 3 -> 5 -> 2
createArrayInReverse(head) == [2,5,3,1]
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work? build the array as you traverse the linked list, reverse the array at the end
Algorithm 1:
Time: O(n)
Space: O(1)
 

📆 PLAN
Outline of algorithm #: 

while the node is not null
  append current node's value to the array
  move to the next node

reverse the array
traverse from both ends of the array inward and swap elements

🛠️ IMPLEMENT
function createArrayInReverse(node) {
def createArrayInReverse(node: Node) -> list[int]:
'''

class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

  def __str__(self):
    if not self.next:
      return str(self.val)
    parts = []
    while self:
      parts.append(str(self.val))
      self = self.next
    return "->".join(parts)
  
def createArrayInReverse(node):
  result = []

  while node:
    result.append(node.val)
    node = node.next

  a = 0
  z = len(result)-1

  while a < z:
    result[a], result[z] = result[z], result[a]
    a +=1
    z -=1  

  return result
'''

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

ll = Node(1, Node(2, Node(3, Node(4))))

ll2 = Node(1)
ll3 = None
ll4 = Node(2, Node(1))
print(createArrayInReverse(ll), "expect [4, 3, 2, 1]")
print(createArrayInReverse(ll2), "expect [1]")
print(createArrayInReverse(ll3), "expect []")
print(createArrayInReverse(ll4), "expect [1, 2]")