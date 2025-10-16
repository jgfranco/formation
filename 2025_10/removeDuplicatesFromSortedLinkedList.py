class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
    def __str__(self):
        nodes = []
        while self:
            nodes.append(str(self.val))
            self = self.next
        return "->".join(nodes)


def removeDuplicates(head):
    if not head: return None

    head.next = removeDuplicates(head.next)

    if head.next and head.next.val == head.val:
        return head.next
    
    return head




list = ListNode(1, ListNode(1, ListNode(2, ListNode(2))))



print(removeDuplicates(list))