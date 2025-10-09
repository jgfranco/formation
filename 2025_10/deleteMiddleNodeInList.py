

"""
Problem Prompt
Given a linked list, delete the middle node of the list in a single pass.
If n is the length of the list, the middle node is* n/2* using zero-based indexing.
Return the head of the modified list.


Example(s)

head = 1
deleteMiddleNodeSinglePass(head)) == "<empty>"

head = 1 -> 2
deleteMiddleNodeSinglePass(head)) == "1"

head = 1 -> 2 -> 3
deleteMiddleNodeSinglePass(head)) == "1 -> 3"


Signature/Prototype
function deleteMiddleNodeSinglePass(head) {
def deleteMiddleNodeSinglePass(head: Node) -> Node:
            s
                    f
        1-> 2-> 3

"""

class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def deleteMiddleNodeSinglePass(head: Node) -> Node:
    if not head or not head.next: return None
    sentinel = Node(-1, head)
    slow = sentinel
    fast = sentinel

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    slow.next = slow.next.next

    return sentinel.next

def toString(head: Node) -> None:
  if not head:
    return "<empty>"

  parts = []
  while head:
    parts.append(str(head.val))
    head = head.next

  return " -> ".join(parts)

head = None
print(toString(deleteMiddleNodeSinglePass(head)) == "<empty>")

head = Node(1) # 1
print(toString(deleteMiddleNodeSinglePass(head)) == "<empty>")

head = Node(1, Node(2)) # 1 -> 2
print(toString(deleteMiddleNodeSinglePass(head)) == "1")

head = Node(1, Node(2, Node(3))) # 1 -> 2 -> 3
print(toString(deleteMiddleNodeSinglePass(head)) == "1 -> 3")

head = Node(4, Node(6, Node(8, Node(3)))) # 4 -> 6 -> 8 -> 3
print(toString(deleteMiddleNodeSinglePass(head)) == "4 -> 6 -> 3")

head = Node(4, Node(6, Node(8, Node(3, Node(4)))))  # 4 -> 6 -> 8 -> 3 -> 4
print(toString(deleteMiddleNodeSinglePass(head)) == "4 -> 6 -> 3 -> 4")

