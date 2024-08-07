class ListNode:
    def __init__(self, value = 0, next = None): 
        self.value = value
        self.next = next

def find_middle(head: ListNode) -> int:
  if not head:
    return None

  slow = head
  fast = head.next

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    
  return slow.value

# Test Cases
LL1 = ListNode(1, ListNode(3, ListNode(5)))
LL2 = ListNode(1, ListNode(3, ListNode(-13, ListNode(-3, ListNode(1)))))
LL3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
LL4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
print(find_middle(None), "expect None") # None
print(find_middle(LL1), "expect 3") # 3
print(find_middle(LL2), "expect -13") # -13
print(find_middle(LL3), "expect 2") # 2
print(find_middle(LL4), "expect 3") # 3
print(find_middle(ListNode(1)), "expect 1") # 1