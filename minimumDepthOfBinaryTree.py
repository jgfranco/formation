'''
https://leetcode.com/problems/minimum-depth-of-binary-tree/

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.


🔎 EXPLORE
What are some other insightful & revealing test cases?
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: traverse tree by level, whenever we find a leaf node return current level
Time: O(n) where n is the number of nodes in the tree
Space: O(n) where n is the number of nodes in the tree
 

📆 PLAN
Outline of algorithm #: 
use a queue to traverse the tree using a queue
initialize a queue
initialize a level count
check for the size of the queue and use that to only pop the size of the queue (by level traversal)
increment level
as soon as we find a leaf node return level

append left node and right node if found

return level

 

🛠️ IMPLEMENT
Write your algorithm.
'''
class TreeNode:
  def __init__(self, value, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right 
  
def minDepth(root):
  from collections import deque
  q = deque([root])
  level = 0
  while q:

    size = len(q)
    level += 1

    for _ in range(size):
      curr = q.popleft()
      if not curr.left and not curr.right: return level

      if curr.left: q.append(curr.left)
      if curr.right: q.append(curr.right)

  return level


'''

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''

tree = TreeNode(3, 
                TreeNode(9),
                TreeNode(20, 
                         TreeNode(15), 
                         TreeNode(7)))

print(f'result: {minDepth(tree)}, expect 2') 