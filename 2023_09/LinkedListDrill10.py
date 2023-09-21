"""Q. Given an unsorted linked list, find the element with the lowest value.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer head

head of the list

[output] integer
"""

class ListNode:
  def __init__(self, value, next = None) -> None:
      self.value = value
      self.next = next
  
def solution(head):
    lowest = float("inf")
    
    while head:
        lowest = min(lowest, head.value)
        head = head.next
        
    return lowest


"""Q. Given a linked list, shift it to the left by one.

Example:
Input: 1 -> 2 -> 3
Output: 2 -> 3 -> 1
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer head

head of the list

[output] linkedlist.integer

head of the updated list
"""

def solution(head):

    if not head or not head.next: return head
    
    curr = head
    newHead = head.next
    while curr.next:
         
        curr = curr.next
        
    curr.next = head
    head.next = None
    
    return newHead

"""Q. Given a linked list and a target, remove all nodes that are NOT the target value

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
def solution(list, target):
    
    prev = None
    curr = list
    
    while curr:
        
        if curr.value != target:
            if prev:
                prev.next = curr.next
                curr = curr.next
                continue
            else:
                list = list.next
                curr = curr.next
                continue
        
        prev = curr
        curr = curr.next
        
    return list

"""Q. Given a linked list of positive integers, find the first element that occurs at least k number of times.

If no element occurs k times, return -1.
You may assume k is greater than zero.
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer head

[input] integer k

[output] integer

first element repeated k times
"""

def solution(head, k):
    countMap = {}
    
    curr = head
    
    while curr:
        countMap[curr.value] = count =  countMap.get(curr.value, 0) +1
        if count == k:
            return curr.value
        curr = curr.next
        
    return -1

"""Q. Given a linked list, insert a node with the value 0 after each existing node. This should double the length of the original list and every other value should be a 0.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer head

[output] linkedlist.integer

head of the list
"""
def solution(head):
    if not head: return None
    
    curr = head
    next= head.next
    
    while curr:
        curr.next = ListNode(0)
        curr.next.next = next
        curr = next
        if curr:
            next = curr.next
    
    return head


"""Q. Given a head of the list and a value x, move all nodes less than x such that they come before nodes greater than or equal to x. The original relative order should be preserved when partitioning.

Examples:

List = 1 -> 3 -> 2 -> 0 -> 4 and x = 3
returns 1 -> 2 -> 0 -> 3 -> 4

List = 1 -> 4 -> 3 -> 2 -> 5 -> 2 -> 7 and x = 3
returns 1 -> 2 -> 2 -> 4 -> 3 -> 5 -> 7

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer head

[input] integer x

[output] linkedlist.integer
"""

def solution(head, x):
    from collections import deque
    lessThan = deque([])
    equalAndGreater = deque([])
    
    curr = head
    
    while curr:
        if curr.value < x:
            lessThan.append(curr.value)
        elif curr.value >= x:
            equalAndGreater.append(curr.value)
        
        curr = curr.next
        
        
    curr = head
    
    while curr:
        if len(lessThan) > 0:
            curr.value = lessThan.popleft()
        elif len(equalAndGreater)  > 0:
            curr.value = equalAndGreater.popleft()
        
        curr = curr.next
        
    return head