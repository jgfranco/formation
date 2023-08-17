"""
🔎 EXPLORE
What are some other insightful & revealing test cases?
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: two pointer method:

  first pointer moves k times forward, second pointer stays behind
  then both pointers move forward until first poiunter reaches the end (None)
  return second pointer
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 

initialize two sentinel nodes:
guide and result

move guide node k times forward
move guide and result nodes forward until guide node is None

return result node

 
🛠️ IMPLEMENT
Write your algorithm.
"""
class Node:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next

  def __str__(self):
    if not self.next:
      return str(self.value)
    parts = []
    while self:
      parts.append(str(self.value))
      self = self.next
    return "->".join(parts)
  
def findKthElementFromEnd(head, k):
    
    guide = Node(None, head)
    result = Node(None, head)

    while guide and k > 0:
      guide = guide.next
      k -=1

    while guide:
      result = result.next
      guide = guide.next
    
    return result.value

""" 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

"""

ll = Node(1, Node(2, Node(3, Node(4, Node(5)))))

print(findKthElementFromEnd(ll, 1), "expect 5")
print(findKthElementFromEnd(ll, 2), "expect 4")
print(findKthElementFromEnd(ll, 3), "expect 3")
print(findKthElementFromEnd(ll, 4), "expect 2")
print(findKthElementFromEnd(ll, 5), "expect 1")
print(findKthElementFromEnd(ll, 6), "expect None")
print(findKthElementFromEnd(ll, 1000), "expect None")
print(findKthElementFromEnd(None, 1000), "expect None")