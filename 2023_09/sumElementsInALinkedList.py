"""
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a linked list, sum all elements in the list.

Examples:
• Given a linked list: 1 ➞ 4 ➞ 5 // returns 10
• Given a linked list: 1 // returns 1

🔎 EXPLORE
What are some other insightful & revealing test cases?
a None LL should return 0, this is also our basecase

🧠 BRAINSTORM
What approaches could work?

Algorithm 1:
use recursion to access the current node's value and add to it the recursive call on the next node
base case would be when we reach the end of the linked list in which case we return 0
Time: O(n) we need to traverse the whole linked list
Space: O(n) when we consider the call stack, 1 call for each node basically


📆 PLAN
Outline of algorithm #: 
recursive function
  basecase: node is none, return 0

  return the current node's value and add the recursive call on the next node

🛠️ IMPLEMENT
Write your algorithm.
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
"""
class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next
        
def sum(node: ListNode) -> int:
  if not node: return 0

  return node.value + sum(node.next)

"""
🧪 VERIFY
Run tests. Methodically debug & analyze issues.

"""
# Test Cases
LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(sum(None)) # 0
print(sum(LL1)) # 10
print(sum(ListNode(1))) # 1