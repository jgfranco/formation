


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def reverse(self, head):
        if not head or not head.next: return head

        curr = head
        prev = None

        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        return prev

    def pairSum(self, head: ListNode) -> int:

        slow, fast = head, head

        while fast:
            slow = slow.next
            fast = fast.next
            if fast: fast = fast.next

        reversedLL = self.reverse(slow) 

        maxSum = float("-inf")

        curr = head
        curr2 = reversedLL

        while curr2:
            maxSum = max(maxSum, curr.val+ curr2.val)
            curr = curr.next
            curr2 = curr2.next
        
        return maxSum
