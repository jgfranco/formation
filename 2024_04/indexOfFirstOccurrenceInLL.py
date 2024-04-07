'''
❓ PROMPT
Given a linked list and a target value, return the index of the first occurrence of that value in the linked list. The index should be zero-indexed.

Example(s)
list1 = 1 -> 2 -> 3 -> 4 -> 5

firstIndexInLL(list1, 9) == -1
firstIndexInLL(list1, 3) == 2
 

🔎 EXPLORE
List your assumptions & discoveries:
base 0 indices
worst case scenario the target node is at the tail of the linked list, so we must 
traverse it in its entirety 

Insightful & revealing test cases:
when the target value is not found, -1 must be returned
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O(n) where n is the number of nodes in the LL,
Space: O(1): no extra space needed for the location of the target node
 

📆 PLAN
Outline of algorithm #: 
create an index variable at 0
traverse iteratively the linked list
  if the current node is the target node:
    return the index
  otherwise 
  increment the index and move on to the next node
 

🛠️ IMPLEMENT
function firstIndexInLL(node, target) 
'''
class Node:
  def __init__(self, value, next = None) -> None:
    self.value = value
    self.next = next
  
def firstIndexInLL(node: Node, target: int) -> int:

  index = 0
  while node:
    if target == node.value:
      return index
    index +=1
    node = node.next

  return -1

'''
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
ll = Node(1, Node(3, Node(5)))

print(firstIndexInLL(ll, 3), "expect 1")
print(firstIndexInLL(ll, 1), "expect 0")
print(firstIndexInLL(ll, 5), "expect 2")
print(firstIndexInLL(ll, 2), "expect -1")