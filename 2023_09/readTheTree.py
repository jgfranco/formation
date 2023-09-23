
'''
❓ PROMPT
In many but not all languages, humans read from top to bottom, left to right. 
This problem is convert a tree to a list of values in this reading order. 
Since computer scientists draw trees with the root at the top, the first node 
we read is that one, followed by the nodes at the first level down (only at 
most two nodes), then the third level, etc. For example:

      a
    /  \
   b     c
 /
d

We would read this as [a, b, c, d].

Write a function that generates a list of the values in a binary tree in this reading order.

Example(s)
treeToArray(new BTNode("a")) - returns ['a']
treeToArray(new BTNode("a", new BTNode("b"))) - only left child, returns ['a', 'b']
treeToArray(new BTNode("a", null, new BTNode("b"))) - only right child, returns ['a', 'b']
treeToArray(new BTNode("a", new BTNode("b"), new BTNode("c"))) - basic tree with both left and right children, , returns ['a', 'b', 'c']

 

🔎 EXPLORE
List your assumptions & discoveries:
this requires level by level traversal of the tree

Insightful & revealing test cases:
 

🧠 BRAINSTORM
What approaches could work?

Algorithm 1: use a queue to visit the nodes on a by level fashion 
Time: O(n) where n represents the number of nodes in the tree
Space: O(n) we will store the nodes temporarily in a queue 
 

📆 PLAN
Outline of algorithm #: 
if the root is None return and empty array
initialize a queue withg the root node
initialize a result array

while there's something in the q
  check the size of the q and store it in a variable called size
  iterate size times
    current node is equal to the result of popleft on the queue
    add current node to the result array
    append the left node and the right node (in that order) to the queue
  
return the result array

🛠️ IMPLEMENT
function treeToArray(root)
function tree_to_array(root):
'''
class TreeNode:
  def __init__(self, value, left = None, right=None) -> None:
    self.value = value
    self.left = left
    self.right = right

def treeToArray(root):
  if not root: return []

  from collections import deque

  q = deque([root])
  result = []

  while q:
    size = len(q)

    for _ in range(size):
      curr = q.popleft()
      result.append(curr.value)

      if curr.left: q.append(curr.left)
      if curr.right: q.append(curr.right)
    
  return result
'''
🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


print(treeToArray(TreeNode("a"))) # returns ['a']
print(treeToArray(TreeNode("a", TreeNode("b")))) # only left child, returns ['a', 'b']
print(treeToArray(TreeNode("a", None, TreeNode("b")))) # only right child, returns ['a', 'b']
print(treeToArray(TreeNode("a", TreeNode("b"), TreeNode("c")))) # basic tree with both left and right children, , returns ['a', 'b', 'c']
print(treeToArray(TreeNode("a", 
                            TreeNode("b", TreeNode("d"), None), 
                            TreeNode("c")))) # returns ['a', 'b', 'c', 'd']