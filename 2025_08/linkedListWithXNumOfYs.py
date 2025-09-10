class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def createLL(count: int, val: int) -> Node:
    if count == 0: return None
    head = Node(val)
    curr = head
    for i in range(count-1):
        curr.next = Node(val)
        curr = curr.next
    
    return head


def toString(head: Node) -> None:
    if not head:
        return "<empty>"

    parts = []
    while head:
        parts.append(str(head.value))
        head = head.next

    return " -> ".join(parts)

print(toString(createLL(0, 1000)) == "<empty>")
print(toString(createLL(1, 999)) == "999")
print(toString(createLL(2, 88)) == "88 -> 88")
print(toString(createLL(3, 4)) == "4 -> 4 -> 4")
print(toString(createLL(5, 3)) == "3 -> 3 -> 3 -> 3 -> 3")
print(toString(createLL(6, 6)) == "6 -> 6 -> 6 -> 6 -> 6 -> 6")
print(toString(createLL(2, -10)) == "-10 -> -10")
print(toString(createLL(3, 0)) == "0 -> 0 -> 0")