"""
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a linked list, append an element with a target value to the list iteratively.

Examples:
• Given a linked list: 1 ➞ 4 ➞ 5, target: 7 // returns 1 ➞ 4 ➞ 5 ➞ 7
• Given a linked list: 0, target 7 // returns 0 ➞ 7


'''
🔎 EXPLORE
What are some other insightful & revealing test cases?
  empty LL, we should handle this case by creating the Node and itsvalue 
  one node existes in the LL, we append to this node
  for any other case (more nodes) we need to navigate to the last node, and assignt its next 
    attribute to the  new node 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: iterative approach
  handle edge cases: No LinkList (None)
Time: O(n) we need to traverse the whole lenght of the linked list
Space: O(1) we are not using extra memory for the solution of this problem
 

📆 PLAN
Outline of algorithm #: 
 
handle the empty case: return a new ListNode with the given value
traverse the linked list until the last node
update the last nodes's next attribute to a new ListNode 

🛠️ IMPLEMENT
Write your algorithm.
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
"""
class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next
        
def arrayify(head):
    array = []
    ptr = head
    while ptr != None:
        array.append(ptr.value)
        ptr = ptr.next
    return array

def append(node: ListNode, target: int) -> ListNode:
  if not node: return ListNode(target)

  root= node
  while node.next:
      node = node.next

  node.next = ListNode(target)
  return root
# Test Cases

LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(arrayify(append(None, 1))) # [1]
print(arrayify(append(LL1, 7))) # [1, 4, 5, 7]
print(arrayify(append(ListNode(), 7))) # [0, 7]