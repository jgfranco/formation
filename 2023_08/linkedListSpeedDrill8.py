class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None



"""
Given an array, create a linked list with its values in the order they appear in the array.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer array

[output] linkedlist.integer

head of the linked list

"""
def solution(array):
    
    current = None
    head = None
    for num in array:
        if not current:
            current = ListNode(num)
            head = current
            continue
        current.next = ListNode(num)
        current = current.next
            
    return head
    

"""
Given a linked list, return the value of the element that is at the 1/3 position from the head.

You may assume the total number of elements is multiples of 3 (e.g. 3, 6, 9, 12 ...).
Examples:

Given a linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 // returns 2
Given a linked list: 1 -> 2 -> 3 // returns 1
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer head

head of the list

[output] integer

one third element's value in the list
"""

def solution(head):
    counter = 0
    
    curr = head
    
    while curr:
        counter +=1
        curr = curr.next
        
    k = counter //3
    
    curr = ListNode(-1)
    curr.next = head
    for i in range(k):
        curr = curr.next
    
    return curr.value

"""
Given a linked list, remove f nodes after k nodes and repeat the process until you reach the end of the list.

Example:
Input: head = 1 → 3 → 3 → 2 → 8 → 2 → 5 → 7 → 10 → 2 → 1, F = 2, K = 3
Output: 1 → 3 → 3 → 2 → 5 → 7 → 1

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer head

head of the input linked list

[input] integer f

[input] integer k

[output] linkedlist.integer

head of the updated list

"""
def solution(head, f, k):
    if k == 0: return []
    if not head: return head
    
    curr = head
    while curr:
        for _ in range(k-1): 
            print("moved forward")
            if curr: curr = curr.next
        
        bridge = curr
        #print(f'curr: {curr.value}, brigde: { bridge.value}')
        
        for j in range(f + 1):
            print(j)
            if bridge: bridge = bridge.next
            print(bridge)
        
        #if bridge:
            #print(f'curr: {curr.value}, bridge: { bridge.value}')
        
        if curr: 
            curr.next = bridge
            
            curr = curr.next
        
    return head
            
"""
Given a linked list, determine if it is a palindrome.

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer head

head of the list

[output] boolean
"""

def solution(head):
    
    array = []
    
    curr = head
    while curr:
        array.append(curr.value)
        curr = curr.next
        
        
    return array == array[::-1]
"""

Q. Given a sorted linked list, remove any nodes with duplicate values.

Example:
Input: 1 → 2 → 2 → 3 → 3 → 3 → 4
Output: 1 → 2 → 3 → 4

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer head

head of the input linked list

[output] linkedlist.integer

head of the updated linked list
"""

def solution(head):
    
    curr = head
    while curr and curr.next:
        
        if curr.value == curr.next.value:
            curr.next = curr.next.next
        else:
            curr = curr.next
            
    return head


"""
Given an unsorted linked list with unique values, insert an element before the target element

If target cannot be found in the list, do nothing.
Example:

Given a linked list: 3 -> -1 -> 2 -> 5, element (to be inserted): 0, target: 2
// returns: 3 -> -1 -> 0 -> 2 -> 5
[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer head

head of the list

[input] integer target

vale of the target node

[input] integer value

value of the node to be inserted before the target node

[output] linkedlist.integer

head of the updated list

"""
def solution(head, target, value):

    prev = None
    curr = head
    
    while curr:
        
        if curr.value == target:
            if prev:
                prev.next = ListNode(value)
                prev = prev.next
            else:
                prev = ListNode(value)
                head = prev
            prev.next = curr
            break
        
        
        prev = curr
        curr = curr.next
        
    return head