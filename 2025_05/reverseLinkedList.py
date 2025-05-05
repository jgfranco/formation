"""
https://leetcode.com/problems/reverse-linked-list/description/?envType=study-plan-v2&envId=leetcode-75
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        """
          p c n
        1 2 3>4>5
         <
        """
        if not head or not head.next:
            return head

        prev = ListNode(-1)
        prev.next = head
        curr = head
        next = head.next

        while curr:
            curr.next = prev
            if prev == head:
                prev.next = None
            prev = curr
            curr = next
            if next:
                next = next.next
            
        return prev