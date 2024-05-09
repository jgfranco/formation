

""" swap adjacent nodes in a linked list"""


class Node:
  def __init__(self, value, next = None) -> None:
    self.value = value
    self.next = next
  
  def __str__(self) -> str:
    result = []

    while self:
      result.append(str(self.value))
      self = self.next
    return "->".join(result)
  


def swapNodes(head):
  if not head or not head.next:
    return head
  
  newHead = head.next
  prev = None
  curr = head

  while curr and curr.next:
    secondNode = curr.next

    if prev:
      prev.next = secondNode

    curr.next, secondNode.next = secondNode.next,curr
    
    prev = curr
    curr = curr.next
    
  return newHead

ll = Node(1, Node(2,
                   Node(3, Node(4))))
print(swapNodes(ll))



'''
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed).

Follow-up:
Another way of stating the initial problem would be to reverse sub-lists of length 2. Write a new version of the function that takes a second parameter, k. For k = 2, the result is just like the original function: adjacent pairs are swapped. But for larger values of k, the function should now reverse longer sub-lists, again modifying the pointers to rethread the list in the new order. As an example, for a list [1 -> 2 -> 3 -> 4 -> 5] we get the following results for different values of k:

k = 2: [2 -> 1 -> 4 -> 3 -> 5]
k = 3: [3 -> 2 -> 1 -> 5 -> 4]
k = 4: [4 -> 3 -> 2 -> 1 -> 5]
k = 5: [5 -> 4 -> 3 -> 2 -> 1]
 

EXAMPLE(S)
Input: (-1)->1->2->3->4
Output: 2->1->3->4
      
prev=new Node(-1)
loop:
  firstNode = head
  secondNode = head.next
  prev.next=secondNode
  firstNode.next=secondNode.next
  secondNode.next=firstNode
  head= firstNode.next
  prev=firstNode
  




prev:3
curr: 4
prev.next=curr.next
curr.next=prev
2->1->3->4

Input: 1->2->3
Output: 2->1->3

# Swap pairs
# Fail quickly by checking for a head and head.next



 

FUNCTION SIGNATURE
def swapPairs(self, head: ListNode) -> ListNode:

      
# prev=new Node(-1)
# loop:
#   firstNode = head
#   secondNode = head.next
#   prev.next=secondNode
#   firstNode.next=secondNode.next
#   secondNode.next=firstNode
#   head= firstNode.next
#   prev=firstNode
  
# function swapPairs(head) {
#   let dummy = new Node('dummy', head);
#   let firstNode = head;
#   let secondNode = head.next;

#   while () {
    
#   }

# }



# prev=new Node(-1)
# loop:
#   firstNode = head
#   secondNode = head.next
#   prev.next=secondNode
#   firstNode.next=secondNode.next
#   secondNode.next=firstNode
#   head= firstNode.next
#   prev=firstNode
class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next


def swapPairs(head):
  dummy = Node(-1, head) 
  prev = dummy
  # (-1)->1->2->3->4
  while(head and head.next):
    # Nodes to swap
    firstNode = head
    secondNode = head.next
    # Swapping logic
    prev.next = secondNode
    firstNode.next  = secondNode.next
    secondNode.next = firstNode
    # Moving Forward
    head = firstNode.next
    prev = firstNode
  # (-1)->2->1->4->3 
  # return new node head
  return dummy.next

def toString(head: Node) -> None:
  theString = ""
  while head:
    theString += str(head.val) + '->'
    head = head.next
  return theString

head = Node(1, Node(2, Node(3, Node(4))))
print(toString(swapPairs(head)) == "2->1->4->3->")

head = Node(1, Node(2, Node(3)))
print(toString(swapPairs(head)) == "2->1->3->")

head = Node(1)
print(toString(swapPairs(head)) == "1->")

print(swapPairs(None) == None)
    
    












###### Brittany

def swapPairs(head):
  
  if not head or not head.next:
    return head
    
  prev = None
  curr = head
  result = head.next

  while curr and curr.next:
    # second_node is to be swapped
    second_node = curr.next

    # link the prev node to the second node
    if prev:
      prev.next = second_node
    
    # swap curr and second_node by pointing curr.next to second_node's next, and second_node.next to curr
    curr.next, second_node.next = second_node.next, curr
    
    # move prev to curr, and curr needs to now be the next pair's first node
    prev, curr = curr, curr.next
  
  return result


'''