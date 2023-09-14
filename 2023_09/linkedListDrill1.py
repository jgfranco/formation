"""
Q. Given an array, create a linked list with its values in the order they appear in the array.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

[output] linkedlist.integer

head of the linked list
"""
#Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def solution(array):
    
    ll = ListNode(-1)
    curr = ll
    
    for item in array:
        curr.next = ListNode(item)
        curr = curr.next
    return ll.next  

"""
Q. Given a linked list, insert a node with the value 0 after each existing node. This should double the length of the original list and every other value should be a 0.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer head

[output] linkedlist.integer

head of the list
"""
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head):
    if not head: return None
    curr = head
    next = head.next
    
    while curr:
        curr.next = ListNode(0)
        curr.next.next = next
        curr = next
        if curr:
            next = curr.next
            
    return head
"""        
  Q. Given a target integer and count integer, create a linked list of length count, where each node has the value target.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer target

[input] integer count

[output] linkedlist.integer

head
"""
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(target, count):
    
    ll = ListNode(-1)
    curr = ll
    
    for _ in range(count):
        curr.next = ListNode(target)
        curr = curr.next
    
    return ll.next

"""
Q. Given a linked list of positive integers, find the first element that occurs at least k number of times.

If no element occurs k times, return -1.
You may assume k is greater than zero.
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer head

[input] integer k

[output] integer

first element repeated k times
"""
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head, k):
    elementMap = {}
    
    curr = head
    
    while curr:
    
        elementMap[curr.value] = currentCount = elementMap.get(curr.value, 0) +1
        if currentCount == k: return curr.value
        
        curr = curr.next
        
    return -1
"""
Q. Given a linked list, limit the number of repetitions to k. Iterate through the linked list, keeping track of how many times the value has been repeated. Once a value has been repeated k target number of times, remove any future instances of that node.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer head

[input] integer k

[output] linkedlist.integer

head of the list

"""
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head, k):
    if k == 0: return None
    prev = None
    
    curr = head
    elementMap = {}

    while curr:
        elementMap[curr.value] = count =  elementMap.get(curr.value, 0) +1
    
        if count > k:
            if prev:
                prev.next = curr.next
                curr = curr.next
                continue
            else:
                head = curr.next
                curr = curr.next
       
        prev = curr
        curr = curr.next
    
    return head

"""
Q. Given a linked list, remove all nodes with an odd value from the list.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer head

head of the list

[output] linkedlist.integer

head of the updated list
"""

# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head):   
    prev = None
    curr = head

    while curr:
    
        if curr.value %2 != 0:
            if prev:
                prev.next = curr.next
                curr = curr.next
                continue
            else:
                head = curr.next
                curr = curr.next
                continue
       
        prev = curr
        curr = curr.next
    
    return head
