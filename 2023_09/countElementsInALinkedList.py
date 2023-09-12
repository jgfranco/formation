'''
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given an unsorted linked list, count the number of elements (iteratively or recursively).

Examples:
• Given a linked list: 1 ➞ 4 ➞ 5 // returns 3
• Given a linked list: 0 // returns 1

🔎 EXPLORE
What are some other insightful & revealing test cases?
 

🧠 BRAINSTORM
What approaches could work? 
  the recursive function should be fairly simple. 
  basecase: return 0 if current node is None

  return 1 plus the recursive call on the next node

Algorithm 1:
Time: O(n) we need the traverse the entirety of the linked list to count its length
Space: O(n) if we consider the call stack
 

📆 PLAN
Outline of algorithm #: 
base case:
  node is none, return 0

  return 1 and add the recursive call on the next node
 

🛠️ IMPLEMENT
Write your algorithm.
'''
class ListNode:
  def __init__(self, value = 0, next = None): 
    self.value = value
    self.next = next
    
def count(node: ListNode) -> int:
  if not node: return 0
  return 1 + count(node.next)
'''

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''
# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(count(None), 'expect 0') 
print(count(LL1), 'expect 3') 
print(count(ListNode()), 'expect 1') 