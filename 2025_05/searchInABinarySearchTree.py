

"""
https://leetcode.com/problems/search-in-a-binary-search-tree/description/?envType=study-plan-v2&envId=leetcode-75
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if not root: return None
        
        if root.val == val: return root

        if val > root.val:
            return self.searchBST(root.right, val)
        
        return self.searchBST(root.left, val)
        