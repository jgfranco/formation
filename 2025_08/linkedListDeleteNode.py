class ListNode:
    def __init__(self, val = 0, next = None):
      self.val = val
      self.next = next

    def __repr__(self):
      return f"{self.val}->{self.next}" if self.next else f"{self.val}"

def build_list(values):
  head = ListNode(values[0])
  curr = head
  for v in values[1:]:
    curr.next = ListNode(v)
    curr = curr.next
  return head

def to_array(head):
  arr = []
  while head:
    arr.append(head.val)
    head = head.next
  return arr

# -- - student implements deleteNode(node) here-- -

def deleteNode(node_to_delete):
  node_to_delete.val = node_to_delete.next.val
  node_to_delete.next = node_to_delete.next.next

# Example 1
head = build_list([4, 5, 1, 9])
node_to_delete = head.next  # Node with value 5
deleteNode(node_to_delete)
assert to_array(head) == [4, 1, 9]

# Example 2: delete a middle node in longer list
head2 = build_list([1, 2, 3, 4, 5])
node_del = head2.next.next  # Node with value 3
deleteNode(node_del)
assert to_array(head2) == [1, 2, 4, 5]

print('All Python tests passed!')

