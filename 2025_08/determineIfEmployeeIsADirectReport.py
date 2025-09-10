

class Node:
    def __init__(self, val, left= None, right = None):
        self.val = val
        self.left = left
        self.right = right

def isDirectReport(person: Node, manager: int, employee: int) -> bool:

    if person is None:
        return False

    if person.val == manager:
        if person.left and person.left.val == employee:
            return True

        if person.right and person.right.val == employee:
            return True
        
        return False
    
    return isDirectReport(person.left, manager, employee) or isDirectReport(person.right, manager, employee)


#     1
#   2   3
#      4  5
#     6  
ceo = Node(1,
        Node(2),
        Node(3,
          Node(4,
            Node(6)),
          Node(5)
      ))

# 5
solo = Node(5)

#   5
# 10
partner = Node(5,
            Node(10)
          )

print(isDirectReport(None, 1, 2) == False)
print(isDirectReport(solo, 1, 2) == False)
print(isDirectReport(partner, 5, 5) == False)
print(isDirectReport(partner, 5, 10) == True)
print(isDirectReport(ceo, 1, 2) == True)
print(isDirectReport(ceo, 1, 4) == False)
print(isDirectReport(ceo, 2, 1) == False)
print(isDirectReport(ceo, 2, 3) == False)
print(isDirectReport(ceo, 3, 1) == False)
print(isDirectReport(ceo, 3, 5) == True)
print(isDirectReport(ceo, 4, 5) == False)
print(isDirectReport(ceo, 4, 6) == True)
print(isDirectReport(ceo, 1, 1) == False)
print(isDirectReport(ceo, 4, 4) == False)