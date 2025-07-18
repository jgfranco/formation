


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        """
             eh
              --------> -----> N
        1    2    3    4    5
                            o. e
         --------> --------->
        """

        if not head or not head.next: return head

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        odd.next = evenHead
        return head
        

        