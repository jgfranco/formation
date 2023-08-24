class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def __str__(self):
        if not self.next:
            return str(self.val)
        parts = []
        while self:
            parts.append(str(self.val))
            self = self.next
        return "->".join(parts)

"""
Given a linked list, remove the head and tail of the list and return the new list

For example, given the list:
1 -> 3 -> 5 -> 2

Return:
3 -> 5

Advice
Try not to limit the number of special cases / if conditions you need.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer list

[output] linkedlist.integer
"""
def solution(list):
    if not list or not list.next: return None
    head = list
    prev = None
    curr = list
    while curr and curr.next:
        prev = curr
        curr= curr.next
        
    if prev: prev.next = None
    return head.next

"""
Q. Remove every kth node in a linked list. k will always be >= 2.

For example, given k = 2 and the linked list:
1 -> 3 -> 6 -> 2

The result will be:
1 -> 6

after removing the 2nd node with value 3 and the 4th node with value 2

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer head

The linked list

[input] integer k

[output] linkedlist.integer

The new linked list
"""
def solution(head, k):
    
    counter = 0
    
    prev = ListNode(-1)
    curr = ListNode(-1)
    curr.next = head
    prev.next = curr
    
    while curr:
        
        print(curr.value, counter)
        if counter % k == 0:
            prev.next = curr.next
            curr = prev.next
            counter +=1
            continue
            
        prev = curr
        curr = curr.next
        counter +=1
        
    return head
        
"""
Given a linked list, remove the center node. If the length of the list is even, remove the first of the two center nodes.

For example, given this list:
1 -> 2 -> 3 -> 4

Return:
1 -> 3 -> 4

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer list

[output] linkedlist.integer
"""
def solution(list):
    if not list: return list
    if not list.next: return None
    fast = list
    slow = ListNode(-1)
    slow.next = list
    prev = None
    while fast:
        fast = fast.next
        if fast: fast = fast.next
        prev = slow
        slow = slow.next
  
    if slow == list:
        return list.next
        
    prev.next = slow.next
    return list
"""    
Given a linked list and a sorted array of ints, remove all nodes at the indices found in the array. Any indices that are past the end of the linked list should be ignored. Note that the indices refer to the indices before any nodes are removed.

Example #1. Given the array [0, 2] and the linked list:
1 -> 3 -> 5 -> 2

We would remove the nodes at indices 0 and 2. Therefore, we would return:
3 -> 2

Example #2. Given the array [1, 3, 4] and the linked list:
1 -> 3 -> 5 -> 2

We would remove the nodes at indices 1, 3 and 4. Since 4 is past the end of the list, we would only remove the nodes at indices 1 and 3. Therefore, we would return:
1 -> 5

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer list

[input] array.integer indices

[output] linkedlist.integer

"""
def solution(list, indices):
    head = list
    counter = -1
    
    prev = ListNode(-1)
    curr = ListNode(-1)
    curr.next = head
    prev.next = curr
    
    while curr:
        
        print(curr.value, counter)
        if counter in indices:
            if curr == head:
                head = head.next
            prev.next = curr.next
            curr = prev.next
            counter +=1
            continue
            
        prev = curr
        curr = curr.next
        counter +=1
        
    return head

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
def solution(head):
    
    counter = 0
    
    prev = ListNode(-1)
    curr = ListNode(-1)
    curr.next = head
    prev.next = curr
    
    while curr:
        
        print(curr.value, counter)
        if counter % 2 == 0:
            prev.next = curr.next
            curr = prev.next
            counter +=1
            continue
            
        prev = curr
        curr = curr.next
        counter +=1
        
    return head

"""
Q. Given a linked list and a target integer, remove all nodes with the value target.

Example:

Given a linked list: 1 -> 2 -> 2-> 3 -> 2, target: 2 // returns 1 -> 3
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer list

head of the list

[input] integer target

target value to be removed

[output] linkedlist.integer

head of the updated list

"""

def solution(list, target):
    head = list
    curr = list
    prev = None

    
    while curr:
        #print(prev.value, curr.value, head.value)
        if curr.value == target:
            if prev:
                prev.next = curr.next
                curr = prev.next
                continue
            else:
                head = head.next
                curr = curr.next
                continue
                
            
        prev = curr
        curr = curr.next
        
    return head