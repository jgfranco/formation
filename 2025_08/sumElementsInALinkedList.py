class ListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def sum_ll(node: ListNode) -> int:

    if not node: return 0

    return node.value + sum_ll(node.next)

def sum_ll_iterative(node: ListNode) -> int:

    total = 0

    while node:
        total += node.value
        node = node.next

    return total




LL1 = ListNode(1, ListNode(4, ListNode(5)))
print(sum_ll(None)) # 0
print(sum_ll(LL1)) # 10
print(sum_ll(ListNode(1))) # 1
print(sum_ll_iterative(None)) # 0
print(sum_ll_iterative(LL1)) # 10
print(sum_ll_iterative(ListNode(1))) # 1
