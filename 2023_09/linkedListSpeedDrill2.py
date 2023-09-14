"""
Q. Given a linked list, turn the value of each node into its index, starting with 0.

For example, given this linked list:
1 -> 5 -> 3

Overwrite the values so that it is:
0 -> 1 -> 2

Parameters
list: ListNode - the head of the list

Return
the head of the list (should be same as the input list)

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer list

The head of the list

[output] linkedlist.integer

The head of the list
"""
# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def solution(list):
    
    curr = list
    counter =0
    
    while curr:
        curr.value = counter
        counter +=1
        curr = curr.next
        
    return list

"""
Q. Given a linked list and a target, remove all nodes that are NOT the target value

For example, given this linked list:
1 -> 5 -> 5 -> 2, target 5

Return this list:
5 -> 5

Parameters
list: ListNode - the head of the list
target: Int - the target number

Return
the head of new list

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer list

The head of the list

[input] integer target

[output] linkedlist.integer

The head of the new list
"""
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(list, target):
    
    prev = None
    curr = list
    
    while curr:
        
        if curr.value != target:
            if prev:
                prev.next = curr.next
            else:
                list = curr.next
            curr = curr.next
            continue
                
            
        prev = curr
        curr = curr.next
        
    return list

"""
Q. Given an integer k, create a linked list representing the first k values of the Fibonacci sequence.

For example, given k = 1, return this list:
1

Given k = 6, return this list:
1 -> 1 -> 2 -> 3 -> 5 -> 8

Return
the head of new list

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer k

The number of fibonacci elements to include

[output] linkedlist.integer

The head of the new list
"""
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(k):
    
    def printLL(head):
        nodes = []
        while head:
            nodes.append(str(head.value))
            head = head.next
        print(nodes)
            
        return ")->(".join(nodes)
    if k == 0: return None
    if k == 1: return ListNode(1)
    a = 1
    b = 1
    
    head = ListNode(1)
    curr = head
    curr.next = ListNode(1)
    curr = curr.next
    
    
    for i in range(2, k):
        a, b = b, a+b
        curr.next = ListNode(b)    
        curr = curr.next
    print(printLL(head))
    return head
"""
Q. Given a linked list, return an array containing all its values.

For example, given:
1 -> 3 -> 6 -> 2

Return:
[1, 3, 6, 2]

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer head

The linked list

[output] array.integer

The array of values
"""
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head):

    curr = head
    
    arr = []
    
    while curr:
        arr.append(curr.value)
        curr = curr.next
        
    return arr

"""
Q. Remove every other node in a linked list, starting from the second node.

For example, given:
1 -> 3 -> 6 -> 2

Return:
1 -> 6

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer head

The linked list

[output] linkedlist.integer

The new linked list
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
    
    counter = 1
    
    while curr:
        
        if counter %2 ==0:
            prev.next = curr.next
            curr = curr.next
            counter +=1
            continue
            
        prev = curr
        curr = curr.next
        counter +=1
        
        
    return head
    

"""
Q. Remove every kth node in a linked list. k will always be >= 2.

For example, given k = 2 and the linked list:
1 -> 3 -> 6 -> 2

The result will be:
1 -> 6

"""
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(head, k):

    prev = None
    curr = head
    
    counter = 1
    
    while curr:
        
        if counter %k ==0:
            prev.next = curr.next
            curr = curr.next
            counter +=1
            continue
            
        prev = curr
        curr = curr.next
        counter +=1
        
        
    return head