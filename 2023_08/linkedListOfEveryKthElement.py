'''
❓ PROMPT
Given a linked list and a target k, return a linked list containing every kth element.

Example(s)
head = 1 -> 3 -> 6 -> 2 -> 8 -> 9
everyKthNode(head, 3) == "6 -> 9"
 

🔎 EXPLORE
List your assumptions & discoveries:
can I make the assumption that if K goes beyond the size of the Linked List the solution should return None

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: traverse the original Linked list with a counter, using modulo find the multiples of K, add only those node to our new Linkedlist
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 
initialize a counter at 1
initialize an empty Linked List

traverse original LL:

  if the counter is a multiple of K: 
    add current node to new linked list

  increment counter

return new LL


 

🛠️ IMPLEMENT
function everyKthNode(node, target) {
def everyKthNode(node: Node, target: int) -> Node:
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
  
def everyKthNode(node, target):
  if target ==1: return node
    
  KLL = None
  counter = 1
  KLLHead = None
  while node:
    if counter % target == 0:
      if KLL:
        KLL.next = Node(node.val)
        KLL = KLL.next
      else:
        KLL = Node(node.val)
        KLLHead = KLL

    node = node.next
    counter +=1
  return KLLHead
'''

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

ll = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6))))))


def toString(head: Node) -> None:
  if not head:
    return "<empty>"

  parts = []
  while head:
    parts.append(str(head.val))
    head = head.next
  return " -> ".join(parts)

# 1 -> 3 -> 6 -> 2 -> 8 -> 9
head = Node(1, Node(3, Node(6, Node(2, Node(8, Node(9))))))
print(toString(everyKthNode(head, 3)) == "6 -> 9")
print(toString(everyKthNode(head, 1)) == "1 -> 3 -> 6 -> 2 -> 8 -> 9")
print(toString(everyKthNode(head, 5)) == "8")
print(toString(everyKthNode(head, 6)) == "9")
print(toString(everyKthNode(head, 7)) == "<empty>")

# 6
head = Node(6)
print(toString(everyKthNode(head, 1)) == "6")
print(toString(everyKthNode(head, 20)) == "<empty>")

# 6 -> 12
head = Node(6, Node(12))
print(toString(everyKthNode(head, 1)) == "6 -> 12")
print(toString(everyKthNode(head, 2)) == "12")

print(toString(everyKthNode(None, 5)) == "<empty>")