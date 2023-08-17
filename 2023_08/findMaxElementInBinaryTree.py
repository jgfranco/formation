"""
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a binary tree, find the element with the largest value.

Example:
• Given a binary tree:
                 1
                / \
               7   3
              / \
             4   5

// returns 7

🔎 EXPLORE
What are some other insightful & revealing test cases?
 
🧠 BRAINSTORM
What approaches could work? 
  the solution should calculate at each step the max between the value at the current node, 
  the max number on the left subtree and the max number on the right subtree

Algorithm 1:
Time: O(n) we need to traverse the whole tree to find the maximum value
Space: O(n) if we consider the stack

📆 PLAN
Outline of algorithm #: 
  basecase: root is None or we found ourselves past a leaf node, return negative infinity
 
🛠️ IMPLEMENT
Write your algorithm.

"""
class TreeNode:
  def __init__(self, value = 0, left = None, right = None):
    self.value = value
    self.left = left
    self.right = right

def tree_max(root: TreeNode):
  # basecase:
  if not root: return float("-inf")

  return max(root.value, tree_max(root.left), tree_max(root.right))

"""
🧪 VERIFY
Run tests. Methodically debug & analyze issues.
"""

print(tree_max(None), float("-inf"))
print(tree_max(TreeNode(1, TreeNode(2), TreeNode(3))), 3) # 3
print(tree_max(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), 29)
print(tree_max(TreeNode(1)), 1)