'''
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
 

EXAMPLE(S)
Input: head = [1,2,3,4,5], k = 2, 4
               L R
Output: [1,4,3,2,5]

k=2, right: 1
k=1, right: 2

 [1,2,3,4,5, 6]

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]


PLAN

dummy = ListNode(None)
dummy.next = head
left = dummy
right = dummy
while k > 0:
  right = right.next
  decrement k

node_a = right

while right is not null:
  increment left by 1
  increment right by 1

node_b.val, node_a.val = node_b.val, node_a.val

return head


FUNCTION SIGNATURE
def swapNodes(self, head: ListNode, k: int) -> ListNode:
'''
'''

[7,9,6,6,7,8,3,0,9,5] k=2
                 L R
'''

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
  def __str__(self):
    values = []

    while self:
      values.append(str(self.val))
      self = self.next

    return "->".join(values)

def swapNodes(head, k):
  if not head:
    return head
  # 1. starting from dummy node, move right pointer k steps
  # guaranteed that k is < len(list)
  left = right = dummy = ListNode(-1, head)
  for _ in range(k):
    right = right.next

  # 2
  nodeA = right
  while right:
    left = left.next
    right = right.next
  
  nodeB = left

  nodeA.val, nodeB.val = nodeB.val, nodeA.val

  return head 


ll= ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
ll2 = None

print(swapNodes(ll, 3))
print(swapNodes(ll, 2))
print(swapNodes(ll, 5))
print(swapNodes(ll2, 0))