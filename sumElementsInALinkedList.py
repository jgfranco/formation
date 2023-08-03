"""
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a linked list, sum all elements in the list.

Examples:
• Given a linked list: 1 ➞ 4 ➞ 5 // returns 10
• Given a linked list: 1 // returns 1

🔎 EXPLORE
What are some other insightful & revealing test cases?
 
🧠 BRAINSTORM
What approaches could work? recursive approach, accumulating the current value and calling on the rest
of the Linked List recursively
Algorithm 1:
Time: O(n) where n is the number of nodes in the linked list
Space: O(n) where n represents the number of calls in the call stack
 
📆 PLAN
Outline of algorithm #: 
 
recursive function 
  base case: node is none, return 0

  return the current value and add the recursive call on the next node


🛠️ IMPLEMENT
Write your algorithm.
 
"""
class ListNode:
  def __init__(self, value = 0, next = None): 
    self.value = value
    self.next = next
        
def sum(node: ListNode) -> int:
  # Write your code here.
  if not node: return 0
  return node.value + sum(node.next)

"""
🧪 VERIFY
Run tests. Methodically debug & analyze issues.
"""
LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(sum(None)) # 0
print(sum(LL1)) # 10
print(sum(ListNode(1))) # 1