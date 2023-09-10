'''
❓ PROMPT
Given the root of a binary tree, return true if the given tree 
is immediately distinct, or false otherwise. A binary tree is 
immediately distinct if no parent node in the tree has a child 
node with the same value as itself.

For example, if the parent node = *1* and it has a child node 
of the same value *1*, this would not be an immediately distinct 
tree. On the other hand, if no nodes have a child node with the 
same value as themselves, this is an immediately distinct tree.

Example(s)
           1*
       1*      2
     3   4   _   6
should return false

           1
       2       2
    5    9   _   _    
should return true
 

🔎 EXPLORE
List your assumptions & discoveries:
 

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?
  traverse iteratively using a queue, at each point check if parent and children have the same value, return false if so
  at the end of the traversal return true, since no such pair was found
Algorithm 1:
Time: O(n) 
Space: O(1)
 

📆 PLAN
Outline of algorithm #: 
initialize queue with root

while there are nodes in the queue:
  pop a node
  if nodes value is equal to left child or right child return false

  add left child to queue
  add right child to queue

return True (no parent was the same to its child)
 

🛠️ IMPLEMENT
function treeIsImmediatelyDistinct(root) {
def treeIsImmediatelyDistinct(root: Node) -> bool:
'''
class TreeNode:
  def __init__(self, value, left = None, right = None) -> None:
    self.value = value
    self.left = left
    self.right = right


def treeIsImmediateDistinct(root):
  from collections import deque
  q = deque([root])

  while q:
    node = q.popleft()

    if node.left: 
      if node.value == node.left.value: return False
      q.append(node.left)
    if node.right:
      if node.value == node.left.value: return False
      q.append(node.right)
  
  return True
'''

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

distinctTree = TreeNode(1, 
                        TreeNode(2, 
                                 TreeNode(1), 
                                 TreeNode(3)), 
                        TreeNode(3))
notDistinctTree = TreeNode(3, 
                           TreeNode(3), 
                           TreeNode(9))

print(treeIsImmediateDistinct(distinctTree), True)
print(treeIsImmediateDistinct(notDistinctTree), False)