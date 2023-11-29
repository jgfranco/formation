'''
❓ PROMPT
Suppose you are given the root of a *Node* class for a supposed N-ary tree.

This *Node* class has a *children* method that returns a list of *Node* children.

However, this tree is actually corrupted! There may be edges in the *children* class that break the basic rules of trees, resulting in possible cycles or multiple parents.

How many edges do you need to remove from this faulty tree to construct a valid tree?

Example(s)
    1
  /   \
  2   3
   \ /
    4
return 1
Explanation: 4 has two parents. We can remove any one of them to create a valid tree.

    1 <--
  /   \ |
  2   3 |
   \    |
    4 --|
return 1
Explanation: 4 loops back to the root (1). We can remove this back edge to create a valid tree.
 

🔎 EXPLORE
List your assumptions & discoveries:
a visited set should help us determine the amount of "errors"
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: traverse the tree-like structure using a queue BFS style
use a visited set, whenever we find a node already in visited set means that we are encountering either a loop
or a node with multiple parents:
Time: O(n) wwe need to visit every node in the tree-like structure
Space: O(n) we are gonna keep a record of every visited node
 

📆 PLAN
Outline of algorithm #: 
 

🛠️ IMPLEMENT
class Node {
  constructor(value, children = []) {
      this.value = value
      this.children = children
  }
}

function edgesAwayFromTree(root) {

class Node:
  def __init__(self, value, children=[]):
    self.value = value
    self.children = children

def edgesAwayFromTree(root: Node) -> int:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

class Node:
  def __init__(self, value, children = []) -> None:
    self.value = value
    self.children = children

def edgesAwayFromTree(root):

  errors = 0
  from collections import deque
  q = deque([root])
  visited = set()

  while q:
    node = q.popleft()

    if node in visited:
      errors +=1
      continue
    else:
      visited.add(node)
      for child in node.children:
        q.append(child)


  return errors

node4 = Node(4)
root = Node(1, [
  Node(2, [node4]),
  Node(3, [node4])
])
print(edgesAwayFromTree(root) == 1)

node4 = Node(4)
root = Node(1, [
  Node(2, [node4]),
  Node(3)
])
node4.children = [root]
print(edgesAwayFromTree(root) == 1)

root = Node(1, [
  Node(2),Node(3)
])
print(edgesAwayFromTree(root) == 0)
  