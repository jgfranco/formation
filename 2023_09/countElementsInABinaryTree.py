"""
▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
✏️ Description
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
Q. Given a binary tree, count the number of elements in the tree.

Example:
• Given a binary tree:
                 1
                / \
               7   3
              / \
             4   5
// returns 5

▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁
🟦 Python
▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔

""" 
class TreeNode:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
"""
🔎 EXPLORE
What are some other insightful & revealing test cases?
 

🧠 BRAINSTORM
What approaches could work?
recursive approach, 
  basecase: current node is None, return 0
  otherwise return 1 and call recursively on left node and right node
Algorithm 1:
Time: O(n) we have to visit every node in the tree
Space: O(n) the amount of calls in the call stack
 

📆 PLAN
Outline of algorithm #: 
recursive function that takes a node

  if the current node is none return 0

  otherwise return 1 + the recursive call on the left node + the recursive call on the right node
 

🛠️ IMPLEMENT
Write your algorithm.
"""
def count_tree(root: TreeNode) -> int:
  if root is None: return 0

  return 1 + count_tree(root.left) + count_tree(root.right)

""" 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

"""
# Test Cases
print(count_tree(None), 0)
print(count_tree(TreeNode(1, TreeNode(2), TreeNode(3))), 3)
print(count_tree(TreeNode(2, TreeNode(29, TreeNode(26)), TreeNode(4, None, TreeNode(2, TreeNode(9))))), 6)
print(count_tree(TreeNode()), 1)