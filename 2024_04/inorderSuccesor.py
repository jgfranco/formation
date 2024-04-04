class Node:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right
    def __str__(self) -> str:
        if self:
          return str(self.val)
        return "None"

def inOrderSuccessor(root: Node, target: int, successor = None) :

    while root:
        if target >= root.val:
            root = root.right
        else:
            successor = root
            root = root.left

    return successor


root = Node(5,
        Node(2, Node(1), Node(4)),
        Node(8, Node(6), Node(9)))

print(inOrderSuccessor(root, 1), "expect 2") 
print(inOrderSuccessor(root, 2), "expect 4") 
print(inOrderSuccessor(root, 4), "expect 5") 
print(inOrderSuccessor(root, 5), "expect 5") 
print(inOrderSuccessor(root, 6), "expect 8") 
print(inOrderSuccessor(root, 8), "expect 9") 
print(inOrderSuccessor(root, 9), "expect None")