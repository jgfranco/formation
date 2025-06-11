
from collections import deque

class Node:
  def __init__(self, val, children= None):
    self.val = val
    self.children = children

  
  def hasPathTo(self, target: int) -> bool:
    q = deque([self])
    visited = set()
    while q:
      node = q.popleft()
      if node.val == target:
        return True
      if node.val not in visited:
        visited.add(node.val)
        if node.children != None:
          q.extend(node.children)
    
    return False
      


example_graph = Node(12, [
  Node(18, [Node(1), Node(4, [Node(3), Node(9)])]),
]);

""" 
                12
                 |
                 18
                 /\
                1  4
                  /\
                 3  9
"""


tests = [
 (9, True),
 (14, False),
 (None, False),
 (3, True)
]

for params, expected in tests:
  actual = example_graph.hasPathTo(params)
  if actual != expected:
    print(f"Test failed for {params}. Expected: {expected}, Actual: {actual}")
  else:
    print(f"Works fine for {params}.")


# cycle
#node4 = Node(4)
#node1 = Node(, [Node(2, node(3, [node4]))])
#node4.children = [node1]


'''
Find Node in Graph (BFS)

Given a starting node in a graph and a target, traverse the graph using BFS and return true if a node with the target value exists, and false otherwise.
 

EXAMPLE(S)
1 --> 2 --> 4
|      \
>       5
3

node is 2 
node.hasPathTo(1) == False



node is 1
node.hasPathTo(3) == True
node.hasPathTo(2) == True
node.hasPathTo(4) == False 
 

FUNCTION SIGNATURE
class Node {
  constructor(val, children = []) {}
  hasPathTo(target) {}
}

class Node:
  def __init__(self, val, children=[]):

  
  def hasPathTo(self, target: int) -> bool:


    

#plan
 for each node intialized call the hasPathTo method.

 perform bfs- checking the current value and it's children if the target value exists
 traverse the array of children within the array. 
 if the target value exists set valueExists to true.

 at the end of searching the children return valueExists

 a form of recursion - once we reach the base case - not return anything. at the end after the method is executed, return valueExists.
 nonlocal valueExists. 

start with a queue with the current node,
visited set
while there are elements in the queue
  popleft
  if current value is the target, return true
  if current value is not in visited:
      add value to visited set

      append all the children to the queue


node1.hasPathTo(2)

q = [node2, node3]
node = q.popleft()

if node.val == target: return true
if node.val is not in visited:
  add node.val to visited
  append all children to q


1 ->2
|
>
3
'''


class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children = [] if children is None else children

from collections import deque
class Node:
  def __init__(self, val, children=[]):
    self.val = val
    self.children = children

  def hasPathTo(self, target: int) -> bool:
    if not self:
      return False

    if self.val == target:
      return True

    queue = deque([self])
    visited = set()

    while queue:
      curr = queue.popleft()

      if curr.val == target:
        return True

      visited.add(curr.val)

      for child in curr.children:
        if child.val not in visited:
          queue.append(child)

    return False