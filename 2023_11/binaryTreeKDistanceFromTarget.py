'''
❓ PROMPT
Given a binary tree, a target node, and integer k, return an array of all node values 
that are k distance away from the target node in any direction. This means we must 
include nodes that can only be reached by going up the tree via parent pointers.

Example(s)
          1
    2          3
 4    5      6     7
8 9 10 11  12 13 14 15

[(1, 0), 2()]
allNodesKDistance(root, 2, 2) == {3,8,9,10,11}
allNodesKDistance(root, 6, 2) == {1,7}
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O()
Space: O()
 

📆 PLAN
Outline of algorithm #: 

1. find the target node

2. create a map where each node points to its parent

3. traverse from target node k times and add nodes at k distance to the result array
      we need a visited set so we dont go back 

 

🛠️ IMPLEMENT
function allNodesKDistance(root, target, k) {
'''
class Node:
  def __init__(self, value, left = None, right = None) -> None:
    self.value = value
    self.left = left
    self.right = right
    
def findTargetNode(root, target):
  from collections import deque
  q = deque([root])
  while q:
    node = q.popleft()
    if node.value == target:
      return node
    if node.left: q.append(node.left)
    if node.right: q.append(node.right)
  return None

def createChildParentMap(root):
  from collections import deque
  q = deque([root])
  childParentMap = {}
  while q:
    node = q.popleft()

    if node.left:
      childParentMap[node.left] = node
      q.append(node.left)
    if node.right:
      childParentMap[node.right] = node
      q.append(node.right)
  return childParentMap

def getNodesAtKDistance(targetNode, childparentMap, k):
  from collections import deque
  q = deque()
  q.append((targetNode, 0))
  result = []
  visited = set()
  visited.add(targetNode)
  while q:
    node, distance = q.popleft()
    if distance == k:
      result.append(node.value)
      continue
    if node in childparentMap and childparentMap[node] not in visited:
      q.append((childparentMap[node], distance+1))
      visited.add(childparentMap[node])
    if node.left and node.left not in visited: 
      q.append((node.left, distance+1))
      visited.add(node.left)
    if node.right and node.right not in visited: 
      q.append((node.right, distance+1))
      visited.add(node.right)
   
  return result
  

def allNodesKDistance(root, target, k):
  targetNode = findTargetNode(root, target)
  if not targetNode: return []

  childParentMap = createChildParentMap(root)

  return getNodesAtKDistance(targetNode, childParentMap, k)


'''
🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

'''
         1
    2          3
 4    5      6     7
8 9 10 11  12 13 14 15
'''
tree1 = Node(1, 
             Node(2, 
                  Node(4, 
                       Node(8),
                       Node(9)),
                  Node(5,
                       Node(10),
                       Node(11))),
             Node(3,
                  Node(6, 
                       Node(12),
                       Node(13)),
                  Node(7, 
                       Node(14),
                       Node(15))))

print(allNodesKDistance(tree1, 2, 1)) # [1,4,5]
print(allNodesKDistance(tree1, 2, 2)) # [3,8,9,10,11]
print(allNodesKDistance(tree1, 2, 3)) # [6,7]
print(allNodesKDistance(tree1, 2, 4)) # [12,13,14,15]
print(allNodesKDistance(tree1, 2, 5)) # []