#.                        n              l
#     1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 


class ListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


def kth_from_last(head: ListNode, k: int) -> int:
    if not head: return None

    slow = head
    fast = head

    for i in range(k):
        if fast: fast = fast.next
        else: return -1

    while fast:
        fast = fast.next
        slow = slow.next
    
    return slow.value




LL1 = ListNode(13, ListNode(1, ListNode(5, ListNode(3, ListNode(7, ListNode(10))))))
print(kth_from_last(LL1, 1)) # 10
print(kth_from_last(LL1, 3)) # 3
print(kth_from_last(LL1, 6)) # 13
print(kth_from_last(LL1, 7)) # -1
print(kth_from_last(None, 7)) # None
