'''
Doubly Linked List Practice

A doubly linked list is a linked list that holds a reference to the next node as well as the previous node. One application for doubly linked lists is implementing an LRU cache.

Implement a DoublyLinkedNode class and the following functions listed below.
 

EXAMPLE(S)
4 <-> 6 <-> 7
add 3
3 <-> 4 <-> 6 <-> 7
add 8
3 <-> 4 <-> 6 <-> 7 <-> 8
add 5
3 <-> 4 <-> 5 <-> 6 <-> 7 <-> 8
 

FUNCTION SIGNATURE
class DoublyLinkedListNode:
  def __init__(self, val, prev=None, next=None):
    pass

# stringify the linked list forwards starting from node. eg: 1 -> 2 -> 3
def stringify(node):
  head = node

  curr = head

  while curr != head
  
  pass

# stringify the linked list backwards starting from node. eg: 3 -> 2 -> 1
def stringifyBackwards(node):
  pass

# return the head of the sorted doubly linked list with the target value added
# node is a reference to a sorted doubly linked list
def insertSorted(head, val):
  pass

# return the head of the sorted doubly linked list with the target value removed
# node is a reference to a sorted doubly linked list
def removeSorted(head, val):
  pass
'''

# if there isn't a node we can just insert it as a single node
# prev.val < val < curr.val or prev.val > val < curr.val
# while curr != head.next
# if prev.val > val 
# head
# tail
# (8) <-> None

# (8)
# next = (8)
# prev = (8)


# val 3
#   h                 t
#   1 <-> 2 <-> 3 <-> 4 
#         p     c 

# p     c     n
# 1 <-> 2 <-> 3 <-> 4 
"""


head == tail
Deleting Node

if head == head.next:
  return None

while curr.val != val
    curr = curr.next

prev = curr.prev
next = curr.next
prev.next = next
next.prev = prev

Inserting Node
  curr = head
  prev = head.prev
  while val>= curr.val
     curr = curr.next
     prev = prev.next
    
  prev.next = newNode
  newNode.next = curr
  newNOde.prev = prev
  curr.prev = newNode
  
 
  

"""
#      head 
#NOne <(8) > NOne

class DoublyLinkedListNode:
  def __init__(self, val, prev=None, next=None):
    self.val = val
    self.prev = prev
    self.next = next

# stringify the linked list forwards starting from node. eg: 1 -> 2 -> 3
def stringify(node):
  if not node: return ""
  
  values = []
  curr = node.next
  head = node

  values.append(str(node.val))

  while curr and curr != head:
    values.append(str(curr.val))
    curr = curr.next
  
  return "<->".join(values)

# stringify the linked list backwards starting from node. eg: 3 -> 2 -> 1
def stringifyBackwards(node):

  if not node:
    return ""

  
  
  curr = node.prev
  head = curr
  expected = str(curr.val)
  curr = curr.prev

  while curr and curr != head:
    expected += "->"
    expected += str(curr.val)
    curr = curr.prev
  
  return expected

# return the head of the sorted doubly linked list with the target value added
# node is a reference to a sorted doubly linked list

# Inserting Node
#   curr = head
#   prev = head.prev
#   while val>= curr.val
#      curr = curr.next
#      prev = prev.next
    
#   prev.next = newNode
#   newNode.next = curr
#   newNOde.prev = prev
#   curr.prev = newNode
  


def insertSorted(head, val):
  
  curr = head
  prev = head.prev

  newNode = DoublyLinkedListNode(val)
  
  while val >= curr.val and curr.next != head:
    prev = curr
    curr = curr.next
  
  prev.next = newNode
  newNode.next = curr
  newNode.prev = prev

# return the head of the sorted doubly linked list with the target value removed
# node is a reference to a sorted doubly linked list
def removeSorted(head, val):

  
  curr = head

  while curr.val != val:
    curr = curr.next
  
  prev = curr.prev
  print(prev.val)
  nxt = curr.next
  print(nxt.val)
  prev.next, nxt.prev = nxt, prev

  if head.val == val: return nxt
  return head


dll = DoublyLinkedListNode(1, None, None)
dll.next = DoublyLinkedListNode(2, dll, None)
dll.next.next = DoublyLinkedListNode(4, dll.next, dll)
dll.prev = dll.next.next

print(stringify(dll))
print(stringifyBackwards(dll))

insertSorted(dll, 3)
print(stringify(dll))

dll = removeSorted(dll, 1)
print(stringify(dll))