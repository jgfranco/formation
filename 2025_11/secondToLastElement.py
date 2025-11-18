

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def secondToLast(head: Node) -> int:
    if head == None or head.next == None:
        return None

    while head.next.next != None:
        head = head.next
    return head.value
        

print(secondToLast(None) == None)

# 1
head = Node(1)
print(secondToLast(head) == None)
  
# 1 -> 2
head = Node(1, Node(2))
print(secondToLast(head) == 1)

       
# 1 -> 2 -> 3
head = Node(1, Node(2, Node(3)))
print(secondToLast(head) == 2)

# 1 -> 2 -> 3 -> 4
head = Node(1, Node(2, Node(3, Node (4))))
print(secondToLast(head) == 3)

# 1 -> 2 -> 3 -> 4 -> 5
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(secondToLast(head) == 4)