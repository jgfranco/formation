"""
Problem Prompt
Given the root of a binary tree, determine whether the tree is symmetric around its center—that is, the left subtree is a mirror reflection of the right subtree. Return true if the tree is symmetric, otherwise return false. Each node contains an integer value and references to its left and right children. Implement a function with the signature below that performs this check.
Example(s)
Input: [1,2,2,3,4,4,3]
Output: true

Input: [1,2,2,null,3,null,3]
Output: false
Signature/Prototype
Python: def isSymmetric(root: Optional[TreeNode]) -> bool
JavaScript: function isSymmetric(root) -> boolean


       1
    2.     2
   3 4    4 3


"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        return 

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root: return True

        def mirror(left, right):

            if not left and not right: return True
            elif not left or not right: return False

            if left.val != right.val: return False

            return mirror(left.left, right.right) and mirror(left.right, right.left)
        
        return mirror(root.left, root.right)



def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node is not None:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root

# ---------- Tests ----------
sol = Solution()
assert sol.isSymmetric(build_tree([1,2,2,3,4,4,3])) is True  # perfectly symmetric
assert sol.isSymmetric(build_tree([1,2,2,None,3,None,3])) is False  # asymmetric structure
assert sol.isSymmetric(build_tree([])) is True  # empty tree
assert sol.isSymmetric(build_tree([1])) is True  # single node
assert sol.isSymmetric(build_tree([1,2,5,3,4,6,7])) is False #symmetric structure, different values
print("All Python tests passed!")


